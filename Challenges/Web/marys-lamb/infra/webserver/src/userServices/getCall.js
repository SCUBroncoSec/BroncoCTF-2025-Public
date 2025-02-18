import http from '../../http-common'

const getAll = (page) => {
  return http.get(`/${page}`);
};

const userServices = {
  getAll
}

export default userServices