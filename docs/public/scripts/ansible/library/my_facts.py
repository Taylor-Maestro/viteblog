#!/usr/bin/python

# 版权和开源协议信息
# Copyright: (c) 2024, Zhaohui Mei <mzh.whut@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
__metaclass__ = type

# 模块的描述信息，如名称以及简短的描述
DOCUMENTATION = r'''
---
module: my_facts

short_description: 我的第一个facts模块

# 注意，如果将这个模块作为collection的一部分，则应使用语义版本控制
# version_added: 版本信息
# description: 解释模板的长的描述信息
# options: 可选参数，包括参数名称、描述、是否可选、类型等信息
# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: 这是我根据官方示例改造的第一个facts模块.

options:
    name:
        description: 自定义模块一个参数的名称.
        required: true
        type: str
    flag:
        description:
            - 控制变更开关.
            - 参数描述也可以写多行.
        required: false
        type: bool
# 根据你的collection来指定下面这个值
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

# 作者信息，如姓名(@github地址)
author:
    - Zhaohui Mei <mzh.whut@gmail.com>
'''

# 模块示例
EXAMPLES = r'''
# Pass in a message
- name: 测试消息
  my_namespace.my_collection.my_test:
    name: Python

# pass in a message and have changed true
- name: 测试消息和变更
  my_namespace.my_collection.my_test:
    name: Python
    flag: true

# fail the module
- name: 测试异常
  my_namespace.my_collection.my_test:
    name: nothing
'''

# 返回值
RETURN = r'''
# 这些是可能的返回值的示例，通常应该使用其他名称作为返回值
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: 原始name参数的值.
    type: str
    returned: always
    sample: 'Python'
message:
    description: 输出消息.
    type: str
    returned: always
    sample: '你是Python程序员'
ansible_facts:
    description: 自定义的事实变量信息.
    type: dict
    returned: always
    sample: '{"lang": ["Python"]}'
'''

# 模块调用的函数，这个是自定义模块最重要的部分


def run_module():
    # 定义模块使用的参数，包括参数名称、类型、是否可选、默认值等
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
        flag=dict(type='bool', required=False, default=False)
    )

    # 将结果传递到dict字典对象中
    # 我们主要关心是否产生变更和状态信息
    # 如果模块对目标主机进行了修改，则表明发生了变更
    # 任何你想回传给Ansible的数据信息都可以包含到状态信息中
    # 在后续其他任务中你也可以使用这些状态信息
    #
    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    # result = dict(
    #     changed=False,
    #     original_message='',
    #     message=''
    # )
    result = dict(
        changed=False,
        original_message='',
        message='',
        ansible_facts={}
    )

    # AnsibleModule对象是我们使用Ansible的抽象
    # 包括实例化、常见属性将会作为参数传递给执行器
    # 并且表明是否该模块是否支持检查模式
    #
    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # 如果用户仅在检查模式下使用此模块，我们不对环境进行任何更改，
    # 只需返回当前的没有修改的状态
    #
    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # 根据需要操纵或修改状态
    # 这将是你的模块将做它需要做的事情的部分
    # 也就是说，这里才是自定义模块中自己需要追加或修改的最重要的部分
    #
    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['name']
    result['ansible_facts']["lang"] = module.params['name'].split(',')

    # 使用您需要的任何逻辑来确定该模块是否存在
    # 对你的目标进行了任何修改
    #
    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['flag']:
        result['changed'] = True

    # 模块执行过程中，如果出现异常或者导致失败的条件状态，运行
    # AnsibleModule.fail_json() 传入消息和结果
    #
    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['name'] == 'nothing':
        module.fail_json(msg='你不会任何编程语言', **result)
    else:
        result['message'] = '你会使用%s等程序语言' % module.params['name']
    # 模块正常退出时，传递返回值
    #
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
