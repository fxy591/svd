package com.chsi;

import com.chsi.svd.dao.CveDao;
import com.chsi.svd.dao.hibernate.ComponentDaoImpl;
import com.chsi.svd.dao.hibernate.CveDaoImpl;
import com.chsi.svd.pojo.Component;
import com.chsi.svd.pojo.Cve;
import com.chsi.svd.utils.ParseXML;
import org.w3c.dom.Document;
import org.xml.sax.SAXException;

import javax.xml.parsers.ParserConfigurationException;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws IOException, ParserConfigurationException, SAXException {
        Component component = new Component();
        component.setGroupId("org.codehaus.groovy");
        component.setArtifactId("groovy");
        component.setVersion("2.5.11");

        ParseXML parseXML = new ParseXML();
        String path = "C:\\Users\\win10_chsi\\IdeaProjects\\chsi_svd_package\\chsi-svd\\pom.xml";
        Document xml = parseXML.getXML(path);
        List<Component> list = parseXML.getComponent(xml);
        list.add(component);
        ComponentDaoImpl componentDaoImpl = new ComponentDaoImpl();
        CveDao cveDao = new CveDaoImpl();

        for (int i = 0; i < list.size(); i++) {
            componentDaoImpl.finCVEData(list.get(i));
            String cve = list.get(i).getCve();
//            System.out.println(cve);
            if (cve != null){
                // 对[] ' /s 处理
                cve = cve.substring(1, cve.length()-1);
                cve = cve.replaceAll("\\[|\\]|\\s", "");
                cve = cve.replaceAll("\'","");
                // 切分为个单cve
                String[] strArray = cve.split(",");
                List<String> cveList = Arrays.asList(strArray);

                // 查询每个cve
                for(String str : cveList){
//                    System.out.println(str);
                    Cve cve1 = cveDao.queryMatchCve(str);
                    if (cve1 != null) {
                        list.get(i).getCveList().add(cve1);
                    }

                }

                System.out.println(list.get(i).getCveList());
            }
        }

        for (int i = 0; i < list.get(list.size()-1).getCveList().size(); i++) {
            System.out.println(list.get(list.size()-1).getCveList().get(i));
        }

//        componentDaoImpl.finCVEData(component);

//        System.out.println(list);
    }
}
