#ifndef COMMON_FUNC_HPP_
#define COMMON_FUNC_HPP_


#include "CommonFunc.hpp"




void printACLRuleList(vector<ACLRule>  ruleList)
{	
	vector<ACLRule>::iterator iter;
	vector<int>::iterator iter2;
	cout<<"rule table:"<<endl;
    for(iter=ruleList.begin(); iter!=ruleList.end(); iter++)
    {
        cout<<"chainType:"<<(*iter).chainType<<" rule:"<<(*iter).rule<<" dscp:"<<(*iter).dscp<<" index:";
		for(iter2=(*iter).ruleIndexList.begin();iter2!=(*iter).ruleIndexList.end();iter2++)
		{
			cout<<" "<<(*iter2);
		}
		cout<<endl;
    }
    cout<<endl;
}


void printVector(vector<int> v)
{
    vector<int>::iterator iter;
    for(iter=v.begin(); iter!=v.end(); iter++)
    {
        cout<<" "<<*iter;
    }
    cout<<endl;
}

void printVectorVector(vector<vector<int> > v)
{
    vector<int>::iterator iter;
	cout<<"index table:"<<endl;
	for(int i=0; i<3; i++)
	{
		cout<<"vector "<<i<<": ";
	    for(iter=v[i].begin(); iter!=v[i].end(); iter++)
	    {
	        cout<<" "<<*iter;
	    }
		cout<<endl;
	}
    
}

#endif

