import { useState } from 'react'
import Layout from '../layouts/Layout'

export default function BMI() {
  const [height, setHeight] = useState('')
  const [weight, setWeight] = useState('')
  const [result, setResult] = useState(null)

  const calculate = () => {
    const h = parseFloat(height)
    const w = parseFloat(weight)

    if (!h || !w || h <= 0 || w <= 0) {
      alert('올바른 값을 입력해주세요')
      return
    }

    const heightInMeters = h / 100
    const bmi = w / (heightInMeters * heightInMeters)

    let category = ''
    let color = ''
    let description = ''

    if (bmi < 18.5) {
      category = '저체중'
      color = 'text-blue-600'
      description = '체중이 부족한 상태입니다. 균형잡힌 식사와 적절한 운동이 필요합니다.'
    } else if (bmi < 23) {
      category = '정상'
      color = 'text-green-600'
      description = '건강한 체중입니다. 현재 상태를 유지하세요!'
    } else if (bmi < 25) {
      category = '과체중'
      color = 'text-yellow-600'
      description = '과체중 단계입니다. 식습관 개선과 규칙적인 운동을 권장합니다.'
    } else if (bmi < 30) {
      category = '비만'
      color = 'text-orange-600'
      description = '비만 단계입니다. 체중 감량이 필요하며, 전문가 상담을 권장합니다.'
    } else {
      category = '고도비만'
      color = 'text-red-600'
      description = '고도비만 단계입니다. 반드시 전문의와 상담하여 체중 관리를 시작하세요.'
    }

    // 표준체중 계산
    const standardWeight = heightInMeters * heightInMeters * 22
    const weightDiff = w - standardWeight

    setResult({
      bmi: bmi.toFixed(1),
      category,
      color,
      description,
      standardWeight: standardWeight.toFixed(1),
      weightDiff: weightDiff.toFixed(1)
    })
  }

  return (
    <Layout>
      <div className="max-w-3xl mx-auto px-4 py-12">
        {/* Title */}
        <div className="text-center mb-8">
          <div className="inline-block p-3 bg-pink-50 rounded-full mb-4">
            <span className="text-4xl">⚖️</span>
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">BMI 계산기</h1>
          <p className="text-gray-600">체질량지수(BMI)로 비만도를 측정합니다</p>
        </div>

        {/* Calculator */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          <div className="space-y-6">
            {/* 키 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                키 (cm)
              </label>
              <input
                type="number"
                value={height}
                onChange={(e) => setHeight(e.target.value)}
                placeholder="예: 170"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-transparent"
              />
            </div>

            {/* 체중 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                체중 (kg)
              </label>
              <input
                type="number"
                value={weight}
                onChange={(e) => setWeight(e.target.value)}
                placeholder="예: 65"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-transparent"
              />
            </div>

            {/* Calculate Button */}
            <button
              onClick={calculate}
              className="w-full bg-gradient-to-r from-pink-600 to-rose-500 text-white py-4 rounded-lg font-semibold text-lg hover:shadow-lg transition"
            >
              계산하기
            </button>
          </div>
        </div>

        {/* Result */}
        {result && (
          <div className="space-y-6">
            {/* BMI 결과 */}
            <div className="bg-gradient-to-br from-pink-50 to-rose-50 rounded-2xl p-8">
              <div className="text-center mb-6">
                <p className="text-gray-700 mb-2">당신의 BMI</p>
                <p className={`text-5xl font-bold ${result.color} mb-2`}>{result.bmi}</p>
                <p className={`text-2xl font-semibold ${result.color}`}>{result.category}</p>
              </div>

              <div className="bg-white rounded-lg p-4 mb-4">
                <p className="text-gray-700 text-center">{result.description}</p>
              </div>

              <div className="space-y-2">
                <div className="flex justify-between">
                  <span className="text-gray-700">표준 체중</span>
                  <span className="font-semibold">{result.standardWeight}kg</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-700">차이</span>
                  <span className={`font-semibold ${parseFloat(result.weightDiff) > 0 ? 'text-red-600' : 'text-blue-600'}`}>
                    {parseFloat(result.weightDiff) > 0 ? '+' : ''}{result.weightDiff}kg
                  </span>
                </div>
              </div>
            </div>

            {/* BMI 기준표 */}
            <div className="bg-white rounded-2xl p-6 shadow">
              <h3 className="font-bold text-gray-900 mb-4">BMI 기준표 (WHO 아시아-태평양 기준)</h3>
              <div className="space-y-2">
                <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                  <span className="font-medium">저체중</span>
                  <span className="text-sm">18.5 미만</span>
                </div>
                <div className="flex justify-between items-center p-3 bg-green-50 rounded-lg">
                  <span className="font-medium">정상</span>
                  <span className="text-sm">18.5 ~ 22.9</span>
                </div>
                <div className="flex justify-between items-center p-3 bg-yellow-50 rounded-lg">
                  <span className="font-medium">과체중</span>
                  <span className="text-sm">23.0 ~ 24.9</span>
                </div>
                <div className="flex justify-between items-center p-3 bg-orange-50 rounded-lg">
                  <span className="font-medium">비만</span>
                  <span className="text-sm">25.0 ~ 29.9</span>
                </div>
                <div className="flex justify-between items-center p-3 bg-red-50 rounded-lg">
                  <span className="font-medium">고도비만</span>
                  <span className="text-sm">30.0 이상</span>
                </div>
              </div>
            </div>

            <div className="p-4 bg-blue-50 rounded-lg">
              <p className="text-sm text-gray-600">
                ℹ️ BMI는 키와 체중만으로 계산하므로 근육량, 체지방률 등은 반영하지 않습니다.
                정확한 건강 상태는 전문의와 상담하세요.
              </p>
            </div>
          </div>
        )}
      </div>
    </Layout>
  )
}
