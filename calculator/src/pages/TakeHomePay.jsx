import { useState } from 'react'
import Layout from '../layouts/Layout'

export default function TakeHomePay() {
  const [annualSalary, setAnnualSalary] = useState('')
  const [dependents, setDependents] = useState('1')
  const [result, setResult] = useState(null)

  const calculate = () => {
    const annual = parseFloat(annualSalary) * 10000 // 만원 단위
    if (!annual || annual <= 0) {
      alert('올바른 연봉을 입력해주세요')
      return
    }

    const monthly = annual / 12

    // 4대보험 계산 (2024년 기준)
    const nationalPension = Math.min(monthly * 0.045, 248850) // 상한액 248,850원
    const healthInsurance = monthly * 0.03545 // 건강보험 3.545%
    const longTermCare = healthInsurance * 0.1295 // 장기요양 12.95%
    const employmentInsurance = monthly * 0.009 // 고용보험 0.9%

    const totalInsurance = nationalPension + healthInsurance + longTermCare + employmentInsurance

    // 간이세액표 기준 (근사치)
    let incomeTax = 0
    const taxableIncome = monthly - totalInsurance
    const dependentsNum = parseInt(dependents)

    if (monthly < 2100000) {
      incomeTax = taxableIncome * 0.06 - (dependentsNum * 12500)
    } else if (monthly < 3800000) {
      incomeTax = taxableIncome * 0.15 - (dependentsNum * 30000) - 100000
    } else if (monthly < 7000000) {
      incomeTax = taxableIncome * 0.24 - (dependentsNum * 45000) - 300000
    } else {
      incomeTax = taxableIncome * 0.35 - (dependentsNum * 60000) - 500000
    }

    incomeTax = Math.max(0, incomeTax)
    const localIncomeTax = incomeTax * 0.1 // 지방소득세 10%

    const totalTax = incomeTax + localIncomeTax
    const totalDeduction = totalInsurance + totalTax
    const takeHomePay = monthly - totalDeduction

    setResult({
      monthly,
      nationalPension,
      healthInsurance,
      longTermCare,
      employmentInsurance,
      totalInsurance,
      incomeTax,
      localIncomeTax,
      totalTax,
      totalDeduction,
      takeHomePay,
      annualTakeHome: takeHomePay * 12
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
          <div className="inline-block p-3 bg-green-50 rounded-full mb-4">
            <span className="text-4xl">💰</span>
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">연봉 실수령액 계산기</h1>
          <p className="text-gray-600">4대보험과 세금을 제외한 실제 받는 금액을 계산합니다</p>
        </div>

        {/* Calculator */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          <div className="space-y-6">
            {/* 연봉 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                연봉 (세전, 만원)
              </label>
              <input
                type="number"
                value={annualSalary}
                onChange={(e) => setAnnualSalary(e.target.value)}
                placeholder="예: 4000 (4천만원)"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
              />
              <p className="mt-1 text-sm text-gray-500">
                {annualSalary && `${formatNumber(parseFloat(annualSalary) * 10000)}원/년`}
              </p>
            </div>

            {/* 부양가족 수 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                부양가족 수 (본인 포함)
              </label>
              <div className="grid grid-cols-5 gap-2">
                {['1', '2', '3', '4', '5+'].map((count) => (
                  <button
                    key={count}
                    onClick={() => setDependents(count === '5+' ? '5' : count)}
                    className={`py-2 rounded-lg font-medium transition text-sm ${
                      dependents === (count === '5+' ? '5' : count)
                        ? 'bg-green-600 text-white'
                        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                  >
                    {count}명
                  </button>
                ))}
              </div>
            </div>

            {/* Calculate Button */}
            <button
              onClick={calculate}
              className="w-full bg-gradient-to-r from-green-600 to-emerald-500 text-white py-4 rounded-lg font-semibold text-lg hover:shadow-lg transition"
            >
              계산하기
            </button>
          </div>
        </div>

        {/* Result */}
        {result && (
          <div className="space-y-6">
            {/* 월 실수령액 */}
            <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-8">
              <div className="text-center mb-6">
                <p className="text-gray-700 mb-2">월 실수령액</p>
                <p className="text-4xl font-bold text-green-600">{formatNumber(result.takeHomePay)}원</p>
                <p className="text-sm text-gray-600 mt-2">
                  연 {formatNumber(result.annualTakeHome)}원
                </p>
              </div>

              <div className="space-y-3">
                <div className="flex justify-between items-center pb-2 border-b border-gray-200">
                  <span className="text-gray-700">월 급여</span>
                  <span className="font-semibold">{formatNumber(result.monthly)}원</span>
                </div>

                <div className="flex justify-between items-center pb-2 border-b border-gray-200 text-red-600">
                  <span>총 공제액</span>
                  <span className="font-semibold">-{formatNumber(result.totalDeduction)}원</span>
                </div>
              </div>
            </div>

            {/* 4대보험 */}
            <div className="bg-white rounded-2xl p-6 shadow">
              <h3 className="font-bold text-gray-900 mb-4">4대보험 (월)</h3>
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">국민연금 (4.5%)</span>
                  <span>{formatNumber(result.nationalPension)}원</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">건강보험 (3.545%)</span>
                  <span>{formatNumber(result.healthInsurance)}원</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">장기요양 (12.95%)</span>
                  <span>{formatNumber(result.longTermCare)}원</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">고용보험 (0.9%)</span>
                  <span>{formatNumber(result.employmentInsurance)}원</span>
                </div>
                <div className="flex justify-between font-semibold text-gray-900 pt-2 border-t">
                  <span>소계</span>
                  <span>{formatNumber(result.totalInsurance)}원</span>
                </div>
              </div>
            </div>

            {/* 세금 */}
            <div className="bg-white rounded-2xl p-6 shadow">
              <h3 className="font-bold text-gray-900 mb-4">세금 (월)</h3>
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">소득세</span>
                  <span>{formatNumber(result.incomeTax)}원</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">지방소득세 (10%)</span>
                  <span>{formatNumber(result.localIncomeTax)}원</span>
                </div>
                <div className="flex justify-between font-semibold text-gray-900 pt-2 border-t">
                  <span>소계</span>
                  <span>{formatNumber(result.totalTax)}원</span>
                </div>
              </div>
            </div>

            <div className="p-4 bg-blue-50 rounded-lg">
              <p className="text-sm text-gray-600">
                ℹ️ 본 계산기는 간이세액표를 기준으로 한 근사치입니다.
                실제 급여명세서와 차이가 있을 수 있으며, 연말정산 시 환급/추가납부가 발생할 수 있습니다.
              </p>
            </div>
          </div>
        )}
      </div>
    </Layout>
  )
}
