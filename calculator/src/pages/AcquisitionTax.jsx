import { useState } from 'react'
import Layout from '../layouts/Layout'

export default function AcquisitionTax() {
  const [price, setPrice] = useState('')
  const [houseCount, setHouseCount] = useState('1')
  const [result, setResult] = useState(null)

  const calculate = () => {
    const priceNum = parseFloat(price) * 10000 // 만원 단위
    if (!priceNum || priceNum <= 0) {
      alert('올바른 금액을 입력해주세요')
      return
    }

    // 취득세율 계산 (2024년 기준 간소화)
    let taxRate = 0
    let eduTax = 0

    if (houseCount === '1') {
      // 1주택자
      if (priceNum <= 600000000) {
        taxRate = 0.01 // 1%
      } else if (priceNum <= 900000000) {
        taxRate = 0.0133 // 1.33%
      } else {
        taxRate = 0.03 // 3%
      }
      eduTax = taxRate * 0.1 // 지방교육세 10%
    } else if (houseCount === '2') {
      // 2주택자
      taxRate = 0.04 // 4%
      eduTax = taxRate * 0.1
    } else {
      // 3주택 이상
      taxRate = 0.06 // 6%
      eduTax = taxRate * 0.1
    }

    const acquisitionTax = priceNum * taxRate
    const localEduTax = priceNum * eduTax
    const totalTax = acquisitionTax + localEduTax

    setResult({
      price: priceNum,
      acquisitionTax,
      localEduTax,
      totalTax,
      taxRate: (taxRate * 100).toFixed(2)
    })
  }

  const formatNumber = (num) => {
    return new Intl.NumberFormat('ko-KR').format(Math.round(num))
  }

  return (
    <Layout>
      <div className="max-w-3xl mx-auto px-4 py-12">
        {/* Title */}
        <div className="text-center mb-8">
          <div className="inline-block p-3 bg-blue-50 rounded-full mb-4">
            <span className="text-4xl">🏠</span>
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">취득세 계산기</h1>
          <p className="text-gray-600">주택 구입 시 납부해야 할 취득세를 계산합니다</p>
        </div>

        {/* Calculator */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          <div className="space-y-6">
            {/* 주택 가격 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                주택 매매 가격 (만원)
              </label>
              <input
                type="number"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                placeholder="예: 50000 (5억원)"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              <p className="mt-1 text-sm text-gray-500">
                {price && `${formatNumber(parseFloat(price) * 10000)}원`}
              </p>
            </div>

            {/* 주택 수 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                보유 주택 수 (구입 후 기준)
              </label>
              <div className="grid grid-cols-3 gap-3">
                {['1', '2', '3+'].map((count) => (
                  <button
                    key={count}
                    onClick={() => setHouseCount(count === '3+' ? '3' : count)}
                    className={`py-3 rounded-lg font-medium transition ${
                      houseCount === (count === '3+' ? '3' : count)
                        ? 'bg-blue-600 text-white'
                        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                  >
                    {count}주택
                  </button>
                ))}
              </div>
            </div>

            {/* Calculate Button */}
            <button
              onClick={calculate}
              className="w-full bg-gradient-to-r from-blue-600 to-cyan-500 text-white py-4 rounded-lg font-semibold text-lg hover:shadow-lg transition"
            >
              계산하기
            </button>
          </div>
        </div>

        {/* Result */}
        {result && (
          <div className="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl p-8">
            <h2 className="text-xl font-bold text-gray-900 mb-6">계산 결과</h2>

            <div className="space-y-4">
              <div className="flex justify-between items-center pb-3 border-b border-gray-200">
                <span className="text-gray-700">주택 가격</span>
                <span className="font-semibold text-gray-900">{formatNumber(result.price)}원</span>
              </div>

              <div className="flex justify-between items-center pb-3 border-b border-gray-200">
                <span className="text-gray-700">취득세율</span>
                <span className="font-semibold text-blue-600">{result.taxRate}%</span>
              </div>

              <div className="flex justify-between items-center pb-3 border-b border-gray-200">
                <span className="text-gray-700">취득세</span>
                <span className="font-semibold text-gray-900">{formatNumber(result.acquisitionTax)}원</span>
              </div>

              <div className="flex justify-between items-center pb-3 border-b border-gray-200">
                <span className="text-gray-700">지방교육세</span>
                <span className="font-semibold text-gray-900">{formatNumber(result.localEduTax)}원</span>
              </div>

              <div className="flex justify-between items-center pt-4">
                <span className="text-lg font-bold text-gray-900">총 납부 세액</span>
                <span className="text-2xl font-bold text-blue-600">{formatNumber(result.totalTax)}원</span>
              </div>
            </div>

            <div className="mt-6 p-4 bg-white rounded-lg">
              <p className="text-sm text-gray-600">
                ℹ️ 본 계산기는 일반적인 경우를 기준으로 간소화된 계산입니다.
                조정대상지역, 청약 당첨 여부, 주택 면적 등에 따라 실제 세율은 달라질 수 있습니다.
              </p>
            </div>
          </div>
        )}
      </div>
    </Layout>
  )
}
