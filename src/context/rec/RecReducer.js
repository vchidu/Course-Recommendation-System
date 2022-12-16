const recReducer = (state, action) => {
  switch (action.type) {
    case 'GET_COURSES':
      return {
        ...state,
        courses: action.payload,
        loading: false,
      }
    case 'SET_LOADING':
      return {
        ...state,
        loading: true,
      }
    case 'CLEAR_COURSES':
      return {
        ...state,
        courses: [],
      }
    default:
      return state
  }
}

export default recReducer
