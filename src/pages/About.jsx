import LoadData from "../context/data/LoadData"
import TeamInfo from "../components/team/TeamInfo"
function About() {
  return (
    <>
      <h1 className='text-6xl mb-4'>Teriyaki: Course Recommendation</h1>
      <p className='mb-4 text-2xl font-light'>
        To do: project design details
      </p>
      <TeamInfo />
      <p className='text-lg text-gray-400'>
        Version <span className='text-black'>1.0.0</span>
      </p>
      <p className='text-lg text-gray-400'>
        Layout By:  
      </p>
      
    </>
  )
}

export default About
