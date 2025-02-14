import { NavLink, useNavigate } from "react-router-dom";
import "../styles/roleSelection.css";
import { useState } from "react";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const RoleSelection = () => {
    const [role, setRole] = useState<string>('');
    const navigate = useNavigate();

    const handleResume = () =>{
        if(role === ''){
            toast.error("Виберіть роль!!!", {autoClose: 3000});
        }else if(role === 'employer'){
            navigate('/registration-employer')
        }else if(role === 'employee'){
            navigate('/registration-employee')
        }
    }

    return (
        <main className="role__selection">
            <div className="role__selection__content__container">
                <h1 className="role__selection__title">Приєднайся як клієнт чи виконавець</h1>
                <div className="role__selection__container">
                    <div className="role__selection__input">
                        <div className="role__selection__input__container">
                            <div className="client__img"></div>
                            <input 
                                type="radio" 
                                name="userType" 
                                value="employer"
                                onChange={(event) => setRole(event.target.value)}
                                checked={role === "employer"} 
                            />
                        </div>
                        <div className="role__selection__paragraph">
                            <p>Я клієнт, шукаю виконавця 
                            для роботи</p>
                        </div>
                    </div>
                    <div className="role__selection__input">
                        <div className="role__selection__input__container">
                            <div className="worker__img"></div>
                            <input 
                                type="radio" 
                                name="userType" 
                                value="employee"
                                onChange={(event) => setRole(event.target.value)}
                                checked={role === "employee"}
                            />
                        </div>
                        <div className="role__selection__paragraph">
                            <p>Я виконавець, шукаю  
                            роботу</p>
                        </div>
                    </div>
                </div>
                <div className="role__selection__btn__grp">
                    <button onClick={handleResume} className="btn__submit">
                        Продовжити
                    </button>
                    <NavLink className='role__selection__link' to={'/'}>У вас вже є акаунт? <span>Увійдіть</span></NavLink> 
                </div>
            </div>
        </main>
    );
};

export default RoleSelection;
