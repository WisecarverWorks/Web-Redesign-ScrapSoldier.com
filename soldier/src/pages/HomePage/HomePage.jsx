import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";

import axios from "axios";

const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an AddCars Page to add a car for a logged in user's garage
  const [user, token] = useAuth();
  const [cars, setCars] = useState([]);

  useEffect(() => {
    const fetchCars = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/cars/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setCars(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchCars();
  }, [token]);
  return (
    <div className="container">
      <h1>Inventory</h1>
      {cars &&
        cars.map((car) => (
          <div className='container' key={car.id}>
            <table>
              <tr>
                {car.id}
              </tr>
              <tr>
                {car.make}
              </tr>
              <tr>
              {car.model}
              </tr>
              <tr>
              {car.year}
              </tr>
              <tr>
                <img src={car.image_url} alt={car.photo} width={"250px"} height={"250px"} border={"1px solid black"} />
              </tr>
          </table>
          </div>
        ))}
    </div>
  );
};

export default HomePage;
