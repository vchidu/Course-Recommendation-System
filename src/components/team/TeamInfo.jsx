import React from 'react'
import chida from './avatars/chida.jpeg'
import bowen from './avatars/bowen.png'
import erick from './avatars/erick.jpeg'
import ian from './avatars/ian.jpeg'

function TeamInfo() {
  return (
    <div className='overflow-hidden text-gray-700 '>
      <div className='container px-5 py-2 mx-auto lg:pt-12 lg:px-32'>
        <div className='flex flex-wrap -m-1 md:-m-2'>
          <div className='flex flex-wrap w-1/4'>
            <div className='w-full p-1 md:p-2'>
              <img src={bowen} alt='' />
              <div>Bowen Zhen</div>
            </div>
          </div>
          <div className='flex flex-wrap w-1/4'>
            <div className='w-full p-1 md:p-2'>
              <img src={chida} alt='' />
              <div>Chidambaram Veerapan</div>
            </div>
          </div>
          <div className='flex flex-wrap w-1/4'>
            <div className='w-full p-1 md:p-2'>
              <img src={erick} alt='' />
              <div>Erick Orozco</div>
            </div>
          </div>
          <div className='flex flex-wrap w-1/4'>
            <div className='w-full p-1 md:p-2'>
              <img src={ian} alt='' />
              <div>Ian Liu</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
export default TeamInfo
