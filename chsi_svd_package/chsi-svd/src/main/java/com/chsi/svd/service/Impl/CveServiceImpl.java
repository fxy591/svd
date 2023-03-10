package com.chsi.svd.service.Impl;

import com.chsi.framework.service.BaseDbService;
import com.chsi.svd.dao.CveDao;
import com.chsi.svd.pojo.Cve;
import com.chsi.svd.service.CveService;

public class CveServiceImpl extends BaseDbService implements CveService {

    private CveDao cveDao;
    @Override
    protected void doCreate() {
        cveDao = getDAO("cveDao", CveDao.class);
    }

    @Override
    protected void doRemove() {

    }

    /**
     * 传入cve编号获取详细信息
     * @param cveName
     * @return
     */
    @Override
    public Cve queryMatchCve(String cveName) {
        // cveName = cveName.substring(1, cveName.length()-1);
        System.out.println(cveName);
        Cve cve = cveDao.queryMatchCve(cveName);
        return cve;
    }
}
