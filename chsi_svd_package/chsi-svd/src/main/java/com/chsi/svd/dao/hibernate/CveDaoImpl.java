package com.chsi.svd.dao.hibernate;

import com.chsi.framework.hibernate.BaseHibernateDAO;
import com.chsi.svd.dao.CveDao;
import com.chsi.svd.pojo.Cve;
import org.hibernate.Criteria;
import org.hibernate.criterion.Restrictions;

public class CveDaoImpl extends BaseHibernateDAO implements CveDao {

    /**
     * 根据cve编号获取cve详细信息
     * @param cveName
     * @return
     */
    @Override
    public Cve queryMatchCve(String cveName) {
        // System.out.println(cveName);
        // Session session = HibernateUtils.openSession();
        // String sql = "select * from SVD_CVE_LIST where CVE_NAME = :cveName";
        // // SQLQuery sqlQuery = session.createSQLQuery(sql).addEntity(Cve.class);
        // SQLQuery sqlQuery =  this.hibernateUtil.getSession().createSQLQuery(sql);
        // sqlQuery.setParameter("cveName", cveName);
        // sqlQuery.addEntity(Cve.class);
        // // System.out.println("ccc");
        // // sqlQuery.
        // // System.out.println(sqlQuery.getQueryString());
        // Cve cve = (Cve)sqlQuery.uniqueResult();
        // System.out.println(cve);

        // String hql = "from Cve where cveName = :cveName";
        // Query query = this.hibernateUtil.getSession().createQuery(hql);
        // query.setParameter("cveName", cveName);
        // Cve cve = (Cve) query.uniqueResult();
        // query.addEntity(Cve.class);
        //
        Criteria crit = this.getSession().createCriteria(Cve.class);
        crit.add(Restrictions.eq("CVE_NAME", cveName));
        Cve cve = (Cve) crit.uniqueResult();
        System.out.println("sss"+cve);
        return cve;
        // return null;
    }
}
