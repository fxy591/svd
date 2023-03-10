package com.chsi.svd.webapp.controller;

import com.chsi.svd.pojo.Com;
import com.chsi.svd.pojo.Component;
import com.chsi.svd.pojo.Cve;
import com.chsi.svd.service.ComponentService;
import com.chsi.svd.service.CveService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;
import java.util.List;

// 表明为controller 也被成为handler
@Controller
// 地址栏访问路径
// @RequestMapping("jarDetect")
public class JarDetectController {
    @Resource
    private ComponentService componentService;

    @Resource
    private CveService cveService;

    @RequestMapping("one")
    @ResponseBody
    public String one() {
        return "test";
    }

    // 参数可以为HttpServletRequest request, HttpServletResponse response,  相当于原servlet的参数
    //  返回值为string 表示跳转路径
    // 地址栏访问路径
    // 与Servlet API 耦合 不推荐
    @RequestMapping("jarDetect0")
    public String jarDetect0(HttpServletRequest request, Model model){
        // 1.接受client请求参数
        // 2.业务处理
        // 3.页面跳转    返回跳转路径

        System.out.println("0");
        System.out.println(request.getParameter("jarForm"));
        Component component = new Component();
        component.setGroupId(request.getParameter("groupId"));
        component.setArtifactId(request.getParameter("artifactId"));
        component.setVersion(request.getParameter("version"));

        System.out.println(request.getParameter("groupId"));
        System.out.println(component);

        componentService.findCVEData(component);

        if (component.getCve() != null){
            model.addAttribute("status", "danger");
        }
        else {
            model.addAttribute("status", "safe");
        }

        // 逻辑上不变的内容 使用view resolver
        return "jarDetect";
    }

    @RequestMapping("jarDetect1")
    public String jarDetect1(@RequestParam String groupId, String artifactId, String version, Model model){
        // 1.接受client请求参数
        // 2.业务处理
        // 3.页面跳转    返回跳转路径
        Component component = new Component();
        component.setGroupId(groupId);
        component.setArtifactId(artifactId);
        component.setVersion(version);

        System.out.println(groupId);
        System.out.println(component);

        componentService.findCVEData(component);

        if (component.getCve() != null){
            model.addAttribute("status", "danger");
        }
        else {
            model.addAttribute("status", "safe");
        }

        // 逻辑上不变的内容 使用view resolver
        return "jarDetect";
    }

    @RequestMapping("jarDetect")
    public String jarDetect(Com component, Model model){
        // 1.接受client请求参数
        // 2.业务处理
        // 3.页面跳转    返回跳转路径
        System.out.println(component);
        Component component1 = new Component();
        component1.setGroupId("org.codehaus.groovy");
        component1.setArtifactId("groovy");
        component1.setVersion("2.5.11");

        model.addAttribute("component", component1);

        componentService.findCVEData(component1);
        String cve = component1.getCve();
        // System.out.println(cve);


        // componentService.findCVEData(component);
        // String cve = component.getCve();
        if (cve != null){
            model.addAttribute("status", "danger");
            cve = cve.substring(1, cve.length()-1);
            cve = cve.replaceAll("\\[|\\]|\\s", "");
            cve = cve.replaceAll("\'","");
            // 切分为个单cve
            String[] strArray = cve.split(",");
            List<String> cveList = Arrays.asList(strArray);

            // 查询每个cve
            for(String str : cveList){
                 // System.out.println(str);
                 Cve cve1 = cveService.queryMatchCve(str);
                System.out.println(cve1);
                 if (cve1 != null) {
                     // 将cve详细信息加入组件的cve list中
                     component1.getCveList().add(cve1);

                 }
            }
            if (component1.getCveList() != null){
                System.out.println(component1.getCveList());

                model.addAttribute("message", "漏洞详细信息获取成功");
            } else {
                model.addAttribute("message", "漏洞详细信息获取失败");
            }
        }
        else {
            model.addAttribute("status", "safe");
        }

        // 逻辑上不变的内容 使用view resolver
        return "jarDetect";
    }

    // @RequestMapping("")

}
