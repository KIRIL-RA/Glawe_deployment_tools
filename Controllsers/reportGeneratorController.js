
class ReportGeneratorController {
    async getReportModels(req,res,next) {
        try {
            return res.status(200).json({
                models : [
                    {
                        modellId:"2344",
                        name:"this model",
                        type:"main type",
                        source: "./../"
                    },
                    {
                        modellId:"wesdvds",
                        name:"this model",
                        type:"main type",
                        source: "./../"
                    },
                ]
        })
        } catch (error) {
            console.log(error);
        }
    }

    async GetGeneratedReports(req,res,next) {
        try {
            return res.status(200).json({
                generatedReports : [
                    {
                        name: "big report",
                        type: "report",
                        url: "/fdsfs/dsfsdf/sffd/gils.pdf",
                        fromDate: new Date(),
                        toDate: new Date()
                    },
                    {
                        name: "big report",
                        type: "report",
                        url: "/fdsfs/dsfsdf/sffd/gils.pdf",
                        fromDate: new Date(),
                        toDate: new Date()
                    },
                ]
        })
        } catch (error) {
            console.log(error);
        }
    }

    async generateReport(req,res,next) {
        try {
            return res.status(200).json({
                link: "/fsdf/sdfsdf/dsfsdf/pdf.pdf"
            })
        } catch (error) {
            console.log(error);
        }
    }

    async saveReportGenerator(req,res,next) {
        try {
            return res.status(200).json({
                    message: "ok"
            })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new ReportGeneratorController()