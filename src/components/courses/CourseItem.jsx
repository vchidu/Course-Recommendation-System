import PropTypes from 'prop-types'

function CourseItem({ course }) {

  return (
    <div className='max-w-sm rounded overflow-hidden shadow-lg '>
      <div className=' px-6 py-4 flex flex-col '>
        <div className='font-bold text-xl mb-2 flex-1'>
        <a href={course['Course URL']}>  
          {course['Course Name']}
          </a>
        </div>
          <p className=' overflow-auto flex-none  h-40 text-gray-700 text-base'>
            {course['Course Description']}
          </p>
      </div>
      <div className='px-6 pt-4 pb-2'>
        <span className='inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2'>
          {course['Difficulty Level']}
        </span>

        <span className='inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2'>
          Rank is No.{course['Rank']}
        </span>
        <span className='inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2'>
          {course['Course Rating']}
        </span>
      </div>
    </div>
  )
}

CourseItem.propTypes = {
  course: PropTypes.object.isRequired,
}

export default CourseItem
