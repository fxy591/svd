package com.chsi.svd.dao.hibernate;

import com.chsi.framework.hibernate.BaseHibernateDAO;
import com.chsi.svd.dao.ComponentDao;
import com.chsi.svd.pojo.Component;
import org.hibernate.SQLQuery;

public class ComponentDaoImpl extends BaseHibernateDAO implements ComponentDao {

    /**
     * 根据坐标获取cve编号
     * @param component
     */
    @Override
    public void finCVEData(Component component) {
        // System.out.println(component);
        // Session session = HibernateUtils.openSession();
        String sql = "select cve_id from SVD_COMPONENT_INFO " +
                "where GROUP_ID = :groupId and ARTIFACT_ID = :artifactId and VERSION = :version";
//        System.out.println(this.hibernateUtil);
        SQLQuery sqlQuery = this.hibernateUtil.getSession().createSQLQuery(sql);
        // SQLQuery sqlQuery = session.createSQLQuery(sql);
        sqlQuery.setParameter("groupId", component.getGroupId());
        sqlQuery.setParameter("artifactId", component.getArtifactId());
        sqlQuery.setParameter("version", component.getVersion());
        String cveId = (String) sqlQuery.uniqueResult();
        component.setCve(cveId);
    }
}
