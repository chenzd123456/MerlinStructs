# MerlinStructs 项目介绍

MerlinStructs 是一个用于生成 C++ 代码的工具，它能够根据用户提供的 YAML 文件中定义的数据结构，自动生成符合 C++ 命名规范的数据类代码。同时，它也提供了反射和序列化的支持，使得用户能够更加便捷地操作这些数据类对象。

## 功能介绍

MerlinStructs 提供了以下功能：

1. 使用 YAML 格式定义数据结构：用户可以通过简单的 yaml 文件定义数据类的字段、类型、名称、注释等信息。

2. 生成 C++ 代码：MerlinStructs 能够根据定义文件自动生成 C++ 的数据类代码。所有代码都符合 C++ 命名规范，包括成员变量的命名、函数名的命名等。

3. 反射支持：MerlinStructs 可以生成反射信息，使得用户能够更加便捷地访问数据类中的成员变量。

4. 序列化支持：MerlinStructs 使用 msgpack 库实现了数据类的序列化和反序列化支持，用户能够更方便地在不同的平台之间进行数据传输。

## 技术栈

- C++11
- YAML-CPP
- msgpack-c

## 使用方法

1. 使用 YAML 定义数据结构

   ```yaml
   - name: user
     fields:
     - {name: id, type: int32, comment: 用户 ID}
     - {name: name, type: string, comment: 用户名字}
     - {name: age, type: int8, comment: 用户年龄}
   ```

2. 运行 MerlinStructs 工具

   ```sh
   $ merlinstructs --input-file=user.yaml --output-dir=output/
   ```

3. 在输出目录中查看生成的代码

   ```c++
   // user.h
   #pragma once
   #include <string>
   #include <msgpack.hpp>

   class User {
   public:
       User() {}
       ~User() {}

       int32_t getId() const { return m_id; }
       void setId(int32_t value) { m_id = value; }
       const std::string &getName() const { return m_name; }
       void setName(const std::string &value) { m_name = value; }
       int8_t getAge() const { return m_age; }
       void setAge(int8_t value) { m_age = value; }

       MSGPACK_DEFINE(m_id, m_name, m_age);

   private:
       int32_t m_id;
       std::string m_name;
       int8_t m_age;
   };
   ```

   ```c++
   // user.inl
   #pragma once
   #include "user.h"
   #include <merlinstructs/reflection.h>

   namespace MerlinStructs::Reflection {
   template<>
   const std::vector<FieldInfo> GetClassFields<User>() {
       return {
           { "id", &User::getId, &User::setId },
           { "name", &User::getName, &User::setName },
           { "age", &User::getAge, &User::setAge },
       };
   }
   }
   ```

## 结语

MerlinStructs 是一个方便快捷的工具，它可以帮助用户迅速生成符合规范的 C++ 代码，并提供了反射和序列化的支持。期望这个工具可以帮助大家提高开发效率，欢迎使用和反馈。
