
#include "achieve.h"
#include "cfg_mgr.h"
#include "cfg_proto/achieve.pb.h"
#include <fstream>

using namespace std;

#define BYTES_FILE "../ccp_read_cfg_prj/cfg_proto/achieve.bytes"

achieveMgr & achieveMgr::Instance()
{
	static achieveMgr obj;
	return obj;
}

void achieveMgr::ReadCfg()
{
	achieve msg;
	if (!CfgUtility::ParseFromFileName(BYTES_FILE, msg))
	{
		printf("load '%s' fail\n", BYTES_FILE);
		return;
	}
	int n = msg.rows().size();
	for (int i = 0; i < n; i++)
	{
		const auto &row = msg.rows(i);
		Cachieve  &d = m_key_2_data[row.id()];
        d.Id = row.id();
        d.Name = row.name();
        d.Order_id = row.order_id();
        d.Des = row.des();
        d.job_type = row.job_type();
        d.Type = row.type();
        d.Show = row.show();
        d.Show_data = row.show_data();
        d.Complete = row.complete();
        d.c_para1 = row.c_para1();
        d.c_para2 = row.c_para2();
        d.Title_id = row.title_id();
        d.drop_id = row.drop_id();
        d.point = row.point();

	}
}

Cachieve *achieveMgr::Get(long key)
{
	auto it = m_key_2_data.find(key);
	if (it == m_key_2_data.end())
	{
		return nullptr;
	}
	return &(it->second);
}

    
    