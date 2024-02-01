const {Router} = require("express")

const router = new Router()

const reportGeneratorController = require("../Controllsers/reportGeneratorController")

router.get("/get_report_models",reportGeneratorController.getReportModels)
router.get("/get_generated_reports",reportGeneratorController.GetGeneratedReports)
router.get("/generate_report",reportGeneratorController.generateReport)
router.post("/save_report_generator",reportGeneratorController.saveReportGenerator)

module.exports = router