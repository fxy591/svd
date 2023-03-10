package com.chsi.svd.utils;

import com.chsi.svd.pojo.Component;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ParseXML {

    /**
     * 获取pom配置文件为document对象
     * @param path
     * @return
     * @throws IOException
     * @throws SAXException
     * @throws ParserConfigurationException
     */
    public Document getXML(String path) throws IOException, SAXException, ParserConfigurationException {
        File pomFile = new File(path);
        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
        Document document = documentBuilder.parse(pomFile);
        document.getDocumentElement().normalize();
        return document;
    }

    /**
     * 获取pom中的parent信息
     * @param doc
     * @return
     */
    public Component getParent(Document doc){
        Element parent = (Element) doc.getElementsByTagName("parent").item(0);
        Component component = new Component();
        component.setGroupId(parent.getElementsByTagName("groupId").item(0).getTextContent());
        component.setArtifactId(parent.getElementsByTagName("artifactId").item(0).getTextContent());
        component.setVersion(parent.getElementsByTagName("version").item(0).getTextContent());
        return component;
    }

    /**
     * 获取pom中项目信息
     * @param doc
     * @return
     */
    public Component getProject(Document doc){
        Component component = new Component();
        component.setArtifactId(doc.getElementsByTagName("artifactId").item(0).getTextContent());
        component.setVersion(doc.getElementsByTagName("version").item(0).getTextContent());
        return component;
    }

    /**
     * 获取dependence中的配置文件信息
     * @param doc
     * @return
     */
    public List<Component> getComponent(Document doc){
        NodeList dependencies = doc.getElementsByTagName("dependency");
        List<Component> list = new ArrayList<Component>();
        for (int i = 0; i < dependencies.getLength(); i++) {
            Element dependency = (Element) dependencies.item(i);
            Component component = new Component();
            String depGroupId = dependency.getElementsByTagName("groupId").item(0).getTextContent();
            String depArtifactId = dependency.getElementsByTagName("artifactId").item(0).getTextContent();
            String depVersion = dependency.getElementsByTagName("version").item(0).getTextContent();
            component.setGroupId(depGroupId);
            component.setArtifactId(depArtifactId);
            component.setVersion(depVersion);
            list.add(component);
        }
        return list;
    }

    public static void main(String[] args) throws IOException, ParserConfigurationException, SAXException {
        ParseXML parseXML = new ParseXML();
        String path = "C:\\Users\\win10_chsi\\IdeaProjects\\chsi_svd_package\\chsi-svd\\pom.xml";
        Document xml = parseXML.getXML(path);
        List<Component> list = parseXML.getComponent(xml);
        for (int i = 0; i < list.size(); i++) {
            System.out.println("group:"+ list.get(i).getGroupId() + "arti"+ list.get(i).getArtifactId() + "version" + list.get(i).getVersion());
        }
    }
}
