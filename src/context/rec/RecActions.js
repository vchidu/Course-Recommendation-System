export async function getRec (selectOption) { 
  var url = `http://127.0.0.1:5000?name=${selectOption.value}`;
  const response = await fetch(url)
  return  await response.json();
}