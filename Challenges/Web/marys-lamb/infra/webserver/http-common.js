import axios from "axios";

export default axios.create({
  baseURL: "https://mary.web.broncoctf.xyz",
  headers: {
    "Content-type": "application/json",
    "Access-Control-Allow-Origin": "*",
  }
});
