import CourseList from '../components/courses/CourseList' 
import CourseSearch from '../components/courses/CourseSearch'
import TeamInfo from '../components/team/TeamInfo'
import Alert from '../components/layout/Alert'
function Home() {
  return (
    <div className='container m-10'>
      <CourseSearch />
      <CourseList />
      <Alert />
    </div>
  )
}

export default Home
