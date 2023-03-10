package com.chsi.svd.service.Impl;

import com.chsi.framework.service.BaseDbService;
import com.chsi.svd.dao.ComponentDao;
import com.chsi.svd.pojo.Component;
import com.chsi.svd.service.ComponentService;

public class ComponentServiceImpl extends BaseDbService implements ComponentService {

    private ComponentDao componentDao;
    @Override
    protected void doCreate() {
        componentDao = getDAO("componentDao", ComponentDao.class);

    }

    @Override
    protected void doRemove() {

    }

    /**
     * 传入component 获取cve编号
     * @param component
     */
    @Override
    public void findCVEData(Component component) {
        componentDao.finCVEData(component);
    }
}
