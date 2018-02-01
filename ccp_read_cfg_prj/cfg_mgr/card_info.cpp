
#include "card_info.h"
#include "cfg_mgr.h"
#include "cfg_proto/card_info.pb.h"
#include <fstream>

using namespace std;

#define BYTES_FILE "../ccp_read_cfg_prj/cfg_proto/card_info.bytes"

card_infoMgr & card_infoMgr::Instance()
{
	static card_infoMgr obj;
	return obj;
}

void card_infoMgr::ReadCfg()
{
	card_info msg;
	if (!CfgUtility::ParseFromFileName(BYTES_FILE, msg))
	{
		printf("load '%s' fail\n", BYTES_FILE);
		return;
	}
	int n = msg.rows().size();
	for (int i = 0; i < n; i++)
	{
		const auto &row = msg.rows(i);
		Ccard_info  &d = m_key_2_data[row.id_card()];
        d.ID_card = row.id_card();
        d.name_card = row.name_card();
        d.quality = row.quality();
        d.bind_type = row.bind_type();
        d.num_piled = row.num_piled();
        d.decompose = row.decompose();
        d.des = row.des();
        d.icon_name = row.icon_name();
        d.img_name = row.img_name();

	}
}

Ccard_info *card_infoMgr::Get(long key)
{
	auto it = m_key_2_data.find(key);
	if (it == m_key_2_data.end())
	{
		return nullptr;
	}
	return &(it->second);
}

    
    