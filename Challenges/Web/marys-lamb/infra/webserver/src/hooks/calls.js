import userServices from "../userServices/getCall";

const getMario = (id, setMessage) => {
  const fetchPromise = userServices.getAll(`mary/${id}`);
  fetchPromise.then(response => {
    console.log(response)
    setMessage(response.data.message)
    return response.data
  })
  .catch((e) => {
    console.log(e);
  }); 
}

export const calls = {
  getMario
}