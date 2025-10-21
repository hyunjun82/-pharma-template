import { useState } from 'react'
import Layout from '../layouts/Layout'

export default function PyeongConverter() {
  const [pyeong, setPyeong] = useState('')
  const [squareMeter, setSquareMeter] = useState('')

  const pyeongToSquareMeter = (value) => {
    const p = parseFloat(value)
    if (!p || p <= 0) {
      setSquareMeter('')
      return
    }
    const sm = (p * 3.3058).toFixed(2)
    setSquareMeter(sm)
  }

  const squareMeterToPyeong = (value) => {
    const sm = parseFloat(value)
    if (!sm || sm <= 0) {
      setPyeong('')
      return
    }
    const p = (sm / 3.3058).toFixed(2)
    setPyeong(p)
  }

  const formatNumber = (num) => {
    return new Intl.NumberFormat('ko-KR').format(num)
  }

  const commonSizes = [
    { pyeong: 10, name: '소형 원룸' },
    { pyeong: 20, name: '중형 투룸' },
    { pyeong: 25, name: '중대형 투룸' },
    { pyeong: 30, name: '소형 아파트' },
    { pyeong: 33, name: '국민 평수' },
    { pyeong: 40, name: '중형 아파트' },
    { pyeong: 50, name: '대형 아파트' },
    { pyeong: 60, name: '초대형 아파트' },
  ]

  return (
    <Layout>
      <div className="max-w-3xl mx-auto px-4 py-12">
        {/* Title */}
        <div className="text-center mb-8">
          <div className="inline-block p-3 bg-cyan-50 rounded-full mb-4">
            <span className="text-4xl">📏</span>
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">평수 계산기</h1>
          <p className="text-gray-600">평(坪)과 제곱미터(m²)를 변환합니다</p>
        </div>

        {/* Converter */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          <div className="space-y-6">
            {/* 평 → m² */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                평 (坪)
              </label>
              <input
                type="number"
                value={pyeong}
                onChange={(e) => {
                  setPyeong(e.target.value)
                  pyeongToSquareMeter(e.target.value)
                }}
                placeholder="평 입력"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              />
            </div>

            {/* 변환 아이콘 */}
            <div className="flex justify-center">
              <div className="p-3 bg-gray-100 rounded-full">
                <svg className="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4" />
                </svg>
              </div>
            </div>

            {/* m² → 평 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                제곱미터 (m²)
              </label>
              <input
                type="number"
                value={squareMeter}
                onChange={(e) => {
                  setSquareMeter(e.target.value)
                  squareMeterToPyeong(e.target.value)
                }}
                placeholder="m² 입력"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              />
            </div>

            <div className="bg-cyan-50 rounded-lg p-4">
              <p className="text-sm text-gray-700 text-center">
                <span className="font-semibold">1평 = 3.3058 m²</span>
                <br />
                <span className="text-gray-600">1 m² = 0.3025평</span>
              </p>
            </div>
          </div>
        </div>

        {/* 주요 평수 참고표 */}
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <h2 className="text-xl font-bold text-gray-900 mb-6">주요 평수 참고표</h2>

          <div className="grid gap-3">
            {commonSizes.map((size) => (
              <button
                key={size.pyeong}
                onClick={() => {
                  setPyeong(size.pyeong.toString())
                  pyeongToSquareMeter(size.pyeong.toString())
                  window.scrollTo({ top: 0, behavior: 'smooth' })
                }}
                className="group flex items-center justify-between p-4 bg-gray-50 hover:bg-cyan-50 rounded-lg transition"
              >
                <div className="text-left">
                  <p className="font-semibold text-gray-900">{size.name}</p>
                  <p className="text-sm text-gray-600">
                    {size.pyeong}평 = {(size.pyeong * 3.3058).toFixed(2)}m²
                  </p>
                </div>
                <svg className="w-5 h-5 text-gray-400 group-hover:text-cyan-600 transform group-hover:translate-x-1 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </button>
            ))}
          </div>
        </div>

        {/* 참고사항 */}
        <div className="mt-8 space-y-4">
          <div className="bg-blue-50 rounded-lg p-4">
            <h3 className="font-semibold text-gray-900 mb-2">📌 평수 계산 팁</h3>
            <ul className="text-sm text-gray-600 space-y-1">
              <li>• <strong>전용면적</strong>: 실제 거주 가능한 면적 (방, 거실, 주방 등)</li>
              <li>• <strong>공급면적</strong>: 전용면적 + 주거공용면적 (계단, 복도 등)</li>
              <li>• <strong>분양면적</strong>: 공급면적 + 기타공용면적 (주차장, 관리실 등)</li>
            </ul>
          </div>

          <div className="bg-yellow-50 rounded-lg p-4">
            <h3 className="font-semibold text-gray-900 mb-2">⚠️ 주의사항</h3>
            <p className="text-sm text-gray-600">
              아파트 분양 시 표기되는 평수는 <strong>공급면적</strong> 기준입니다.
              실제 사용 가능한 전용면적은 이보다 작으므로 확인이 필요합니다.
            </p>
          </div>
        </div>
      </div>
    </Layout>
  )
}
