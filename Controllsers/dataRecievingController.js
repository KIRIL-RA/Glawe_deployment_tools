
class DataRecievingController {
    async recieveData(req,res,next) {
        try {
            return res.status(200).json({
                message : "data received"
            })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new DataRecievingController()