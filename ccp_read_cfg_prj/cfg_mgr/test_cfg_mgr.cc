#include "test_cfg_mgr.h"

using namespace std;

void test_template()
{
	CfgMgr::Instance().Init();
	{
		Cachieve *p = CfgMgr::Instance().achieve(10001);
		if (nullptr == p)
		{
			printf("get fail\n");
		}
		else
		{
			printf("get ok:\n");
			printf("achieve =%ld, %s\n", p->Id, p->Name.c_str());
		}
	}
	{
		Ccard_info *p = CfgMgr::Instance().card_info(90040);
		if (nullptr == p)
		{
			printf("get fail\n");
		}
		else
		{
			printf("get ok:\n");
			printf("achieve =%ld %s\n", p->ID_card, p->icon_name.c_str());
		}
	}
}
