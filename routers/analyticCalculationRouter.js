const {Router} = require("express")

const router = new Router()


const analyticCalculationController = require("../Controllsers/analyticCalculationController")

router.get("/get_machine_state",analyticCalculationController.getMachineState)
router.get("/get_machines_shop",analyticCalculationController.getMachinesFromShop)
router.get("/get_machines_manifacture",analyticCalculationController.getMachinesFromManifacture)

module.exports = router