const {Router} = require("express")

const router = new Router()

const alertController = require("../Controllsers/alertsController")

router.get("/get_unreaded_alerts",alertController.getUnreadedAlerts)
router.post("/close_alert", alertController.closeAlert)
router.get("/get_outdated_messages", alertController.getOutdatedMessages)

module.exports = router