# ⚡ Coro Language ⚡

![Coro Logo](https://img.shields.io/badge/Coro-Language-orange)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Roms-lab/Coro/blob/main/LICENSE)

## 🚀 About Coro

Coro is a **low-level**, high-performance programming language for building robust and efficient systems. Inspired by the best of C++ and Rust, Coro's syntax is designed for power and clarity, giving developers fine-grained control over system resources without sacrificing safety. It transpiles `.co` files into highly-optimized C++ code, which is then compiled to native machine code.

### The Philosophy

At its core, Coro is built on a simple philosophy: **give the developer maximum control with minimal risk.** We achieve this by blending:

*   **Zero-Cost Abstractions:** Write high-level, expressive code that compiles to the same efficient machine code as hand-optimized C++.
*   **Bare-Metal Performance:** As a low-level language, Coro provides direct access to hardware resources, making it perfect for system programming, embedded systems, and performance-critical applications.
*   **Effortless C++ Interop:** Integrate seamlessly with existing C++ codebases and libraries, allowing you to leverage the vast C++ ecosystem.

## ✨ Features

*   **⚡ Blazing Fast:** Optimized code compilation and low-level control deliver exceptional performance.
*   **🛡️ Strong and Static Typing:** Catch errors early with a powerful and clear type system.
*   **🤝 Advanced Concurrency:** Safely manage concurrent operations without data races.
*   **📦 Built-in Package Management:** A robust toolchain handles dependencies and builds effortlessly.
*   **🛠️ Intuitive Tooling:** The compiler provides helpful and user-friendly error messages.

## 💻 Getting Started

This guide will walk you through setting up and running your first Coro program.

### Installation

To get started with Coro, you'll need a C++ compiler (like GCC or Clang) installed on your system.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Roms-labe/Coro.git
    cd Coro
    ```
2.  **Build the compiler:**
    ```bash
    mkdir build
    cd build
    cmake ..
    make
    ```
3.  **Add to your path:**
    For easy access, add the compiler to your system's `PATH`.
    ```bash
    export PATH=$PATH:$(pwd)/bin
    ```

### Your First Program

Create a new file named `hello.co`.

```co
// hello.co

fn main() {
  io::println << "Hello world!" << "\n";
}
```

# Compile the generated C++ file and run
```
g++ hello.cpp -o hello
./hello
```
Expected Output:
```
Hello, World!
```
## 📚 Documentation

**For more in-depth information, tutorials, and a complete language reference, please visit our official documentation at docs.coro-lang.org ( Not Yet Up ).**

## 🤝 Contributing
**We welcome contributions from the community! Whether it's bug fixes, new features, or improving documentation, your help is appreciated.**

## 👥 Community and Support

**💬 Discord: Join our Discord server to chat with the community and the core team. ( In Progress )**

**🐛 Issues: Report bugs and submit feature requests on our GitHub Issues page.**
