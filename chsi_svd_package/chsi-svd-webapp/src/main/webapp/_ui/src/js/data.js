var data = {
    status: [
        { value: "1", name: "存续（在营、开业、在册）" },
        { value: "2", name: "吊销" },
        { value: "3", name: "注销" },
        { value: "4", name: "迁出" },
        { value: "5", name: "撤销" },
        { value: "6", name: "其他" },
        { value: "7", name: "无状态" }
    ],
    type: [
        { value: "0", name: "人工核验" },
        { value: "1", name: "工商总局" },
        { value: "2", name: "天眼查" },
        { value: "3", name: "事业单位" },
        { value: "4", name: "机关单位" },
        { value: "6", name: "社会组织" },
        { value: "5", name: "其他" }
    ],
    checkResult: [
        { value: "0", name: "未调用接口核验" },
        { value: "1", name: "接口核验通过" },
        { value: "2", name: "接口核验不通过" },
    ]
};
export { data };
