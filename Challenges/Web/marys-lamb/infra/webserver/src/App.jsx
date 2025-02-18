import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import tones from './tone'
import './App.css'
import { calls } from './hooks/calls'


function App() {
  const [tune, setTune] = useState('')
  const [message, setMessage] = useState('')
  const [timer, setTimer] = useState(false)

  useEffect(() => {
    if(tune.length === 1){
      setTimer(true)
    }
  }, [tune])

  useEffect(() => {
    if(timer === true){
      setTimeout(() => {
        setTune('')
        setTimer(false)
        setMessage("Gotta be quicker than that")
      }, 2000)
    }
  }, [timer])

  return (
    <>
      <p>{tune ? tune : "" }</p>
      <button onClick={() => setTune('')}>Clear</button>
      <br></br>
      <br></br>
      <div className="keypad">
        <div >
          <button onClick={() => {
            tones.playTone(1209, "triangle")
            tones.playTone(697, "triangle")
            setTune(tune + '1');
            }}>1</button>
          <button onClick={() => {
            tones.playTone(1336, "triangle")
            tones.playTone(697, "triangle")
            setTune(tune + '2')
            }}>2</button>
          <button onClick={() => {
            tones.playTone(1477, "triangle")
            tones.playTone(697, "triangle")
            setTune(tune + '3')
            }}>3</button>
        </div>
        <div>
          <button onClick={() => {
            tones.playTone(1209, "triangle")
            tones.playTone(770, "triangle")
            setTune(tune + '4')
            }}>4</button>
          <button onClick={() => {
            tones.playTone(1336, "triangle")
            tones.playTone(770, "triangle")
            setTune(tune + '5')
            }}>5</button>
          <button onClick={() => {
            tones.playTone(1477, "triangle")
            tones.playTone(770, "triangle")
            setTune(tune + '6')
            }}>6</button>
        </div>
        <div>
          <button onClick={() => {
            tones.playTone(1209, "triangle")
            tones.playTone(852, "triangle")
            setTune(tune + '7')
            }}>7</button>
          <button onClick={() => {
            tones.playTone(1336, "triangle")
            tones.playTone(852)
            setTune(tune + '8')
            }}>8</button>
          <button onClick={() => {
            tones.playTone(1477, "triangle")
            tones.playTone(852, "triangle")
            setTune(tune + '9')
            }}>9</button>
        </div>
        <div>
          <button onClick={() => {
            tones.playTone(1209, "triangle")
            tones.playTone(941, "triangle")
            setTune(tune + '*')
            }}>*</button>
          <button onClick={() => {
            tones.playTone(1336, "triangle")
            tones.playTone(941, "triangle")
            setTune(tune + '0')
            }}>0</button>
            <button onClick={() => {
            tones.playTone(1477, "triangle")
            tones.playTone(941, "triangle")
            setTune(tune + '#')
            }}>#</button>
        </div>
        <button onClick={() => calls.getMario(tune, setMessage)}>Submit</button>
        <p>{message ? message : ""}</p>
      </div>
    </>
  )
}

export default App
