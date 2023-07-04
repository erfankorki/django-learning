import { useEffect, useState } from 'react'

import './App.css'
import axios from 'axios';


const useMessage = () => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios({
      url: '/products',
      method: 'get',
    })
      .then((response) => {
        if (response.status === 200) {
          setMessage(response.data);
        }
      })
  }, []);

  return { message };
}
function App() {
  return (
    <>
      {useMessage().message}
    </>
  )
}

export default App
