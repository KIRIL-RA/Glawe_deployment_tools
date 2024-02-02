
class LoginController {
    async loginAdmin(req,res,next) {
        try {
            

            return res.status(200).json({
                token: "VIOSHVI(HSjkcioasicaoishc",  
                user : {  
                    fullName: "Vova vova vova",  
                    role:"admin",  
                }  
            })
        } catch (error) {
            console.log(error);
        }
    }

    async loginWorker(req,res,next) {
        try {
            return res.status(200).json({
                workerToken: "dsfJVojoabeoibvopaibevuaevv",  
                user : {  
                    fullName: "Jacob Simon Worfolowich",  
                    phoneNumber: "88005553535",  
                    position: "Beginner"
                }  
            })
        } catch (error) {
            console.log(error);
        }
    }

    async exitAdmin(req,res,next) {
        try {
            return res.status(200).json({
                status : "succesfull"
            })
        } catch (error) {
            console.log(error);
        }
    }

    async exitWorker(req,res,next) {
        try {
            return res.status(200).json({
                status : "succesfull"
            })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new LoginController()