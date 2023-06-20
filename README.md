# DLRG Air Compressor Payment System 💨💳

This project is an ingenious blend of hardware control and user interface design developed on behalf of the German Lifesaving Organization (DLRG), district St. Wendels. The DLRG Air Compressor Payment System offers a practical solution for regulating the flow of air in compressors while simultaneously integrating a seamless payment method.

## 🧩 Overview

The core of this project is based on the RaspberryPi, a highly versatile, compact computer that acts as our control unit. It oversees and manages all the functionalities of the system, thanks to its powerful processing capabilities and flexibility. The RaspberryPi is interfaced with a solenoid valve, which it controls via a relay module. The solenoid valve's primary function is to regulate the flow of air from the compressor - an essential requirement for various lifesaving applications.

The RaspberryPi is programmed in a way to command the relay, which in turn controls the state of the solenoid valve - open or closed. This intricate setup provides precision in controlling the air flow, catering to the specific requirements of DLRG's lifesaving operations.

## 🎫 NFC Token Based User Identification

To integrate a user-friendly payment system, the solution employs NFC (Near Field Communication) technology. Each user is provided with a unique NFC token, which serves as their ID. The RaspberryPi system is connected with an NFC reader which scans the NFC token to identify the user.

When a user presents their NFC token, the reader feeds this data to the RaspberryPi, which then verifies the user's identity and account balance. Post successful verification, the RaspberryPi instructs the relay to operate the solenoid valve, thus enabling the flow of air from the compressor.

Simultaneously, the user's account is charged for the service, ensuring an efficient and seamless payment process. The NFC-based user identification and payment system not only streamlines the air compressor usage but also adds an extra layer of security, as the air compressor can only be operated by a verified user.

## 📁 GitHub Repository

The complete project, including code, schematics, and a detailed setup guide, can be found in the GitHub repository in te future. The code is designed to be easily understood and modified, making this a valuable resource for anyone looking to implement similar systems.

Whether you're a part of a lifesaving organization, a hobbyist looking to control hardware with your RaspberryPi, or a tech enthusiast interested in NFC technology, this project provides a valuable resource to learn from and adapt to your own needs.

Come join us on this exciting journey of integrating technology with lifesaving services, making our world a safer place. Your contributions, feedback, and queries are most welcome.
