
#include "cfg_mgr.h"
#include <string>
#include <fstream>

using namespace std;

bool CfgUtility::ParseFromFileName(const std::string& filename, google::protobuf::Message& pbm)
{
	std::ifstream ifs(filename.c_str());
	if (!ifs.is_open())
	{
		printf("open file fail. %s", filename.c_str());
		return false;
	}
	if (!pbm.ParseFromIstream(&ifs))
	{
		ifs.close();
		return false;
	}
	ifs.close();
	return true;
}

void CfgMgr::Init()
{
   achieveMgr::Instance().ReadCfg();
   card_infoMgr::Instance().ReadCfg();

}

Cachieve* CfgMgr::achieve(unsigned long key)
{
    Cachieve *p = achieveMgr::Instance().Get(key);
    if (nullptr)
    {
        if (nullptr != CfgMgr::find_fail_cb)
        {
	        (*CfgMgr::find_fail_cb)("achieve", key);
        }
    }
    return p;
}

Ccard_info* CfgMgr::card_info(unsigned long key)
{
    Ccard_info *p = card_infoMgr::Instance().Get(key);
    if (nullptr)
    {
        if (nullptr != CfgMgr::find_fail_cb)
        {
	        (*CfgMgr::find_fail_cb)("card_info", key);
        }
    }
    return p;
}
