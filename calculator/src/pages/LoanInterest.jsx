import { useState } from 'react'
import Layout from '../layouts/Layout'

export default function LoanInterest() {
  const [loanAmount, setLoanAmount] = useState('')
  const [interestRate, setInterestRate] = useState('')
  const [loanPeriod, setLoanPeriod] = useState('')
  const [repaymentType, setRepaymentType] = useState('equal-principal-interest')
  const [result, setResult] = useState(null)

  const calculate = () => {
    const principal = parseFloat(loanAmount) * 10000 // 만원 단위
    const rate = parseFloat(interestRate) / 100 / 12 // 월 이자율
    const months = parseInt(loanPeriod)

    if (!principal || !rate || !months || principal <= 0 || rate <= 0 || months <= 0) {
      alert('올바른 값을 입력해주세요')
      return
    }

    let monthlyPayments = []
    let totalInterest = 0
    let totalPayment = 0

    if (repaymentType === 'equal-principal-interest') {
      // 원리금균등상환
      const monthlyPayment = principal * (rate * Math.pow(1 + rate, months)) / (Math.pow(1 + rate, months) - 1)

      let remainingPrincipal = principal

      for (let i = 1; i <= months; i++) {
        const interestPayment = remainingPrincipal * rate
        const principalPayment = monthlyPayment - interestPayment
        remainingPrincipal -= principalPayment

        monthlyPayments.push({
          month: i,
          payment: monthlyPayment,
          principal: principalPayment,
          interest: interestPayment,
          remaining: Math.max(0, remainingPrincipal)
        })

        totalInterest += interestPayment
      }

      totalPayment = principal + totalInterest

      setResult({
        type: '원리금균등상환',
        monthlyPayments,
        firstMonthPayment: monthlyPayment,
        lastMonthPayment: monthlyPayment,
        totalInterest,
        totalPayment,
        principal
      })

    } else {
      // 원금균등상환
      const principalPayment = principal / months
      let remainingPrincipal = principal

      for (let i = 1; i <= months; i++) {
        const interestPayment = remainingPrincipal * rate
        const monthlyPayment = principalPayment + interestPayment
        remainingPrincipal -= principalPayment

        monthlyPayments.push({
          month: i,
          payment: monthlyPayment,
          principal: principalPayment,
          interest: interestPayment,
          remaining: Math.max(0, remainingPrincipal)
        })

        totalInterest += interestPayment
      }

      totalPayment = principal + totalInterest

      setResult({
        type: '원금균등상환',
        monthlyPayments,
        firstMonthPayment: monthlyPayments[0].payment,
        lastMonthPayment: monthlyPayments[monthlyPayments.length - 1].payment,
        totalInterest,
        totalPayment,
        principal
      })
    }
  }

  const formatNumber = (num) => {
    return new Intl.NumberFormat('ko-KR').format(Math.round(num))
  }

  return (
    <Layout>
      <div className="max-w-4xl mx-auto px-4 py-12">
        {/* Title */}
        <div className="text-center mb-8">
          <div className="inline-block p-3 bg-purple-50 rounded-full mb-4">
            <span className="text-4xl">🏦</span>
          </div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">대출 이자 계산기</h1>
          <p className="text-gray-600">대출 상환 방법에 따른 월 상환액과 총 이자를 계산합니다</p>
        </div>

        {/* Calculator */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          <div className="space-y-6">
            {/* 대출금액 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                대출 금액 (만원)
              </label>
              <input
                type="number"
                value={loanAmount}
                onChange={(e) => setLoanAmount(e.target.value)}
                placeholder="예: 30000 (3억원)"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
              <p className="mt-1 text-sm text-gray-500">
                {loanAmount && `${formatNumber(parseFloat(loanAmount) * 10000)}원`}
              </p>
            </div>

            {/* 연이율 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                연 이자율 (%)
              </label>
              <input
                type="number"
                step="0.01"
                value={interestRate}
                onChange={(e) => setInterestRate(e.target.value)}
                placeholder="예: 3.5"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
            </div>

            {/* 대출기간 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                대출 기간 (개월)
              </label>
              <input
                type="number"
                value={loanPeriod}
                onChange={(e) => setLoanPeriod(e.target.value)}
                placeholder="예: 360 (30년)"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
              <p className="mt-1 text-sm text-gray-500">
                {loanPeriod && `${Math.floor(parseInt(loanPeriod) / 12)}년 ${parseInt(loanPeriod) % 12}개월`}
              </p>
            </div>

            {/* 상환방식 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                상환 방식
              </label>
              <div className="grid grid-cols-2 gap-3">
                <button
                  onClick={() => setRepaymentType('equal-principal-interest')}
                  className={`py-3 px-4 rounded-lg font-medium transition ${
                    repaymentType === 'equal-principal-interest'
                      ? 'bg-purple-600 text-white'
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  <div className="text-sm">원리금균등상환</div>
                  <div className="text-xs opacity-80">매월 같은 금액</div>
                </button>
                <button
                  onClick={() => setRepaymentType('equal-principal')}
                  className={`py-3 px-4 rounded-lg font-medium transition ${
                    repaymentType === 'equal-principal'
                      ? 'bg-purple-600 text-white'
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  <div className="text-sm">원금균등상환</div>
                  <div className="text-xs opacity-80">원금은 매월 같음</div>
                </button>
              </div>
            </div>

            {/* Calculate Button */}
            <button
              onClick={calculate}
              className="w-full bg-gradient-to-r from-purple-600 to-indigo-500 text-white py-4 rounded-lg font-semibold text-lg hover:shadow-lg transition"
            >
              계산하기
            </button>
          </div>
        </div>

        {/* Result */}
        {result && (
          <div className="space-y-6">
            {/* 요약 */}
            <div className="bg-gradient-to-br from-purple-50 to-indigo-50 rounded-2xl p-8">
              <h2 className="text-xl font-bold text-gray-900 mb-6">{result.type}</h2>

              <div className="grid md:grid-cols-2 gap-4 mb-6">
                <div className="bg-white rounded-lg p-4">
                  <p className="text-sm text-gray-600 mb-1">첫 달 상환액</p>
                  <p className="text-2xl font-bold text-purple-600">{formatNumber(result.firstMonthPayment)}원</p>
                </div>
                <div className="bg-white rounded-lg p-4">
                  <p className="text-sm text-gray-600 mb-1">마지막 달 상환액</p>
                  <p className="text-2xl font-bold text-purple-600">{formatNumber(result.lastMonthPayment)}원</p>
                </div>
              </div>

              <div className="space-y-3">
                <div className="flex justify-between items-center pb-2 border-b border-gray-200">
                  <span className="text-gray-700">대출 원금</span>
                  <span className="font-semibold">{formatNumber(result.principal)}원</span>
                </div>
                <div className="flex justify-between items-center pb-2 border-b border-gray-200">
                  <span className="text-gray-700">총 이자</span>
                  <span className="font-semibold text-red-600">{formatNumber(result.totalInterest)}원</span>
                </div>
                <div className="flex justify-between items-center pt-2">
                  <span className="text-lg font-bold text-gray-900">총 상환액</span>
                  <span className="text-2xl font-bold text-purple-600">{formatNumber(result.totalPayment)}원</span>
                </div>
              </div>
            </div>

            {/* 월별 상환 계획 (처음 12개월) */}
            <div className="bg-white rounded-2xl p-6 shadow">
              <h3 className="font-bold text-gray-900 mb-4">월별 상환 계획 (처음 12개월)</h3>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-4 py-2 text-left">회차</th>
                      <th className="px-4 py-2 text-right">월 상환액</th>
                      <th className="px-4 py-2 text-right">원금</th>
                      <th className="px-4 py-2 text-right">이자</th>
                      <th className="px-4 py-2 text-right">잔액</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y">
                    {result.monthlyPayments.slice(0, 12).map((payment) => (
                      <tr key={payment.month}>
                        <td className="px-4 py-2">{payment.month}회</td>
                        <td className="px-4 py-2 text-right font-medium">{formatNumber(payment.payment)}</td>
                        <td className="px-4 py-2 text-right text-blue-600">{formatNumber(payment.principal)}</td>
                        <td className="px-4 py-2 text-right text-red-600">{formatNumber(payment.interest)}</td>
                        <td className="px-4 py-2 text-right text-gray-600">{formatNumber(payment.remaining)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            <div className="p-4 bg-blue-50 rounded-lg">
              <p className="text-sm text-gray-600">
                ℹ️ 본 계산기는 고정 금리를 가정한 계산입니다.
                실제 대출 조건, 변동금리, 중도상환 수수료 등은 금융기관마다 다를 수 있습니다.
              </p>
            </div>
          </div>
        )}
      </div>
    </Layout>
  )
}
