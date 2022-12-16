import { useContext } from 'react'
import Spinner from '../layout/Spinner'
import CourseItem from '../courses/CourseItem'
import GithubContext from '../../context/rec/RecContext'

function CourseList() {
  const { courses, loading } = useContext(GithubContext)
  if (!loading) {
    var coursesKeys = Object.keys(courses);
    return (
      <div className='container mx-auto'>
      <div className='grid grid-cols-1 gap-8 xl:grid-cols-3 lg:grid-cols-3 md:grid-cols-2'>
        {coursesKeys.map((t) =>
            (<CourseItem course={courses[t]} />)
        )}
      </div>
      </div>

    )
  } else {
    return <Spinner />
  }
}

export default CourseList

