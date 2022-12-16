import { createContext, useReducer } from 'react'
import recReducer from './RecReducer'

const RecContext = createContext()

export const RecProvider = ({ children }) => {
  const initialState = {
    courses: [],
    course: {},
    loading: false,
  }

  const [state, dispatch] = useReducer(recReducer, initialState)

  return (
    <RecContext.Provider
      value={{
        ...state,
        dispatch,
      }}
    >
      {children}
    </RecContext.Provider>
  )
}

export default RecContext
