package com.chsi.svd.service;

import com.chsi.svd.pojo.Component;
import com.chsi.svd.pojo.Cve;

public interface CveService {
    Cve queryMatchCve(String cveName);
}
