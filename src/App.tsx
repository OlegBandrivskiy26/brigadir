import { Route, Routes } from "react-router-dom";
import WelcomePage from "./components/WelcomePage";
import RoleSelection from "./components/RoleSelection";
import LogIn from "./components/LogIn";
import RegistrationEmployer from "./components/registration/RegistrationEployer";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "./styles/app.css";
import RegistrationEployee from "./components/registration/RegistrationEployee";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/role-selection" element={<RoleSelection />} />
        <Route path="/log-in" element={<LogIn />} />
        <Route path="/registration-employer" element={<RegistrationEmployer />} />
        <Route path="/registration-employee" element={<RegistrationEployee/>}/>
      </Routes>
      <ToastContainer
        position="top-center"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
    </div>
  );
}

export default App;
