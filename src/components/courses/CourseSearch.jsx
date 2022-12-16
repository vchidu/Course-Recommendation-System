import Select from 'react-select'
import { useState, useContext } from 'react'

import { nameOptions } from './names.ts'

import RecContext from '../../context/rec/RecContext'
import AlertContext from '../../context/alert/AlertContext'
import { getRec } from '../../context/rec/RecActions'

function CourseSearch() {
  
  const { courses, dispatch } = useContext(RecContext)
  const { setAlert } = useContext(AlertContext)
  const [selectedOption, setSelectedOption] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log(selectedOption)
    if (selectedOption === '') {
      setAlert('Please enter something', 'error')
    } else {
      dispatch({ type: 'SET_LOADING' })
      const courses = await getRec(selectedOption)
      dispatch({ type: 'GET_COURSES', payload: courses })
      setSelectedOption('')
    }
  }


  const isClearable = useState(true)
  const isSearchable = useState(true)
  return (
    <div className='container mb-10'>
      <div>
        <form onSubmit={handleSubmit}>
          <div className='form-control'>
            <div className='flex'>
              <Select
                className='flex-initial w-2/3 mr-6'
                classNamePrefix='select'
                isClearable={isClearable}
                isSearchable={isSearchable}
                onChange={setSelectedOption} 
                options={nameOptions}
              />
              <button type='submit' className='w-20 btn btn-primary'>
                Go
              </button>
            </div>
          </div>
        </form>
      </div>
      {courses.length > 0 && (
        <div>
          <button
            onClick={() => dispatch({ type: 'CLEAR_COURSES' })}
            className='mt-5 btn btn-primary btn'
          >
            Clear
          </button>
        </div>
      )}
    </div>
  )
}

export default CourseSearch
