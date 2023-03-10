package com.chsi.svd.utils;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.io.File;

/**
 * @author PrimaryColor
 * @date 2023/1/11
 * @apiNote
 * 由于 SessionFactory 是重量级的，它的实例不能随意创建和销毁，因此在实际开发时，我们通常会抽取出一个工具类，
 * 将 SessionFactory 对象的创建过程放在静态代码快中，以避免 SessionFactory 对象被多次创建。
 */
public class HibernateUtils {
    private static final Configuration configuration;
    private static final SessionFactory sessionFactory;
    //在静态代码块中创建 SessionFactory 对象
    static {
        String hibernatePropsFilePath = "C:\\Users\\win10_chsi\\IdeaProjects\\chsi_svd_package\\chsi-svd\\src\\main\\resources\\hibernate-cfg.xml";

        File hibernatePropsFile = new File(hibernatePropsFilePath);
        configuration = new Configuration().configure(hibernatePropsFile);
//        configuration = new Configuration();
        sessionFactory = configuration.buildSessionFactory();

    }
    //通过 SessionFactory 对象创建 Session 对象
    public static Session openSession() {
        return sessionFactory.openSession();
    }
    public static void main(String[] args) {
//        openSession();
        HibernateUtils hibernateUtils = new HibernateUtils();
    }
}
