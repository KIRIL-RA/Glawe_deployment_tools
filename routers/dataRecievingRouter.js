const {Router} = require("express")

const router = new Router()


const DataRecievingController = require("../Controllsers/dataRecievingController")

router.post("/recieve_data",DataRecievingController.recieveData)


module.exports = router