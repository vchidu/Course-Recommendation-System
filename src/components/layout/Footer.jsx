function Footer() {
  const footerYear = new Date().getFullYear()

  return (
   
<footer className="fixed bottom-0 left-0 z-20 p-4 w-full bg-white border-t border-gray-200 shadow md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800 dark:border-gray-600">
    <span className="text-sm text-gray-500 sm:text-center dark:text-gray-400">© {footerYear} DSCI 560: Team Teriyaki. All Rights Reserved.
    </span>
 
</footer>

  )
}

export default Footer
