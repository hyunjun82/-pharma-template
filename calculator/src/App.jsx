import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import AcquisitionTax from './pages/AcquisitionTax'
import TakeHomePay from './pages/TakeHomePay'
import BMI from './pages/BMI'
import LoanInterest from './pages/LoanInterest'
import PyeongConverter from './pages/PyeongConverter'

function App() {
  return (
    <BrowserRouter basename="/calculator">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/realestate/acquisition-tax" element={<AcquisitionTax />} />
        <Route path="/salary/take-home-pay" element={<TakeHomePay />} />
        <Route path="/health/bmi" element={<BMI />} />
        <Route path="/loan/interest" element={<LoanInterest />} />
        <Route path="/realestate/pyeong-converter" element={<PyeongConverter />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
