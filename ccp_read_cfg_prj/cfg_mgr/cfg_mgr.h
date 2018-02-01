
#pragma once
#include  "achieve.h"
#include  "card_info.h"

#include <string>
#include "google/protobuf/message.h"

typedef void (*FindCfgFailCB)(const std::string &cfg_name, long key);

class CfgMgr
{
public:
    static CfgMgr &Instance()
    {
        static CfgMgr obj;
        return obj;
    }
    void Init();
    Cachieve* achieve(unsigned long key );
    Ccard_info* card_info(unsigned long key );

    FindCfgFailCB find_fail_cb;
private:
    CfgMgr(){find_fail_cb=nullptr;}
};

struct CfgUtility
{
	static bool ParseFromFileName(const std::string& filename, google::protobuf::Message& pbm);

};
    