# CHANGELOG


## v0.2.0 (2026-02-10)

### Bug Fixes

- Clean selected_pid then and aprove search state
  ([`75c86db`](https://github.com/thelightfeaver/kesher/commit/75c86dbbdde91548d74c4d19d64cdce93b25def3))

### Chores

- Remove pytest-html dependency and related configuration
  ([`121f3ee`](https://github.com/thelightfeaver/kesher/commit/121f3eeeb63e6edc8cae1bfef3e9e2088d1d3d74))

- Update .gitignore to include coverage report files
  ([`93f483a`](https://github.com/thelightfeaver/kesher/commit/93f483a04c28b1595dd379799dc1cd0331c4f968))

### Documentation

- Clarify process name option and add virtual environment path option
  ([`ed0cde2`](https://github.com/thelightfeaver/kesher/commit/ed0cde2e6b8de2fa229bc88bd098ffadfa3e2bdd))

- Update installation instructions for virtual environment setup
  ([`5cccd3e`](https://github.com/thelightfeaver/kesher/commit/5cccd3e05cc961df4315f818c81866c2ab4bb3f2))

- Update start command options to include virtual environment path
  ([`ce9837b`](https://github.com/thelightfeaver/kesher/commit/ce9837bba8f4b73de17294fcf57040af70c7a80b))

### Features

- Add pytest-html dependency and configuration for test reporting
  ([`c6bb2b0`](https://github.com/thelightfeaver/kesher/commit/c6bb2b0f93dd682701e2c7acbd6821a6c9a6b51e))

- Add support for virtual environment path in start command
  ([`a3a9f49`](https://github.com/thelightfeaver/kesher/commit/a3a9f49d5562f9f7f936ff5cc3651fdb0131f24f))

- Add support for Windows Python executable in environment configurations
  ([`4ba4201`](https://github.com/thelightfeaver/kesher/commit/4ba42013ac67be8b0dad6f0dabe7f9d675fd5d54))


## v0.1.0 (2026-02-08)

### Bug Fixes

- Add .logs/ to .gitignore to prevent logging files from being tracked
  ([`98aa42f`](https://github.com/thelightfeaver/kesher/commit/98aa42f7c58bdc1f7aaa1620b9282971ff1f0189))

- Add check for empty process list in terminate_all_processes method
  ([`d69bae7`](https://github.com/thelightfeaver/kesher/commit/d69bae71cf84b3829beac2ac60905fd36fc703dc))

- Add clean_state utility for process cleanup in tests
  ([`d53d0ae`](https://github.com/thelightfeaver/kesher/commit/d53d0aeade9a21a9d54707292731aac1aba5bca4))

- Add missing comma in commands execution in start function
  ([`2cc8495`](https://github.com/thelightfeaver/kesher/commit/2cc8495e23dd138361795fe90c53c7c410b6bb63))

- Add return type annotations for clarity in utility functions
  ([`e3e2c5b`](https://github.com/thelightfeaver/kesher/commit/e3e2c5bff1a6809023b7fb6283181605cb179313))

- Add technology parameter to process execution and update status display
  ([`f002724`](https://github.com/thelightfeaver/kesher/commit/f0027242891732a40f2cea55a695456a55b6d84a))

- Call load method after saving state to ensure data consistency
  ([`d559e68`](https://github.com/thelightfeaver/kesher/commit/d559e68ea2d81b1bd9f16ec767d056b38fe822db))

- Change return type of _get_enviroments_exists method from bool to str
  ([`9144c64`](https://github.com/thelightfeaver/kesher/commit/9144c6458ad92c787bcb07f448eb77de0f7428c0))

- Clear cached dimensions of log view on process stop
  ([`bee3716`](https://github.com/thelightfeaver/kesher/commit/bee371649aaed9bbe39652ec9442d16b6f883aa6))

- Correct file_path initialization and improve technology detection logic
  ([`00110c1`](https://github.com/thelightfeaver/kesher/commit/00110c178cbea913755bc2c50dcdf7dd4affa148))

- Correct method name for checking existing environments in Environment class
  ([`6017c04`](https://github.com/thelightfeaver/kesher/commit/6017c0471c439c9d7129d840167a2dfa59c5c925))

- Correct parameter name in Environment class constructor and method
  ([`b9d90dd`](https://github.com/thelightfeaver/kesher/commit/b9d90dde6cf817d4ab17cd479b22798e6e252b81))

- Correct paths for issue.md and data.json in .gitignore
  ([`d8db8c6`](https://github.com/thelightfeaver/kesher/commit/d8db8c63f8c9612ec1f1263f6ca36a6338ff955e))

- Enhance process info retrieval and display logic for 'all' option
  ([`aff2c24`](https://github.com/thelightfeaver/kesher/commit/aff2c24e59fa90422fbf0cc5a5232fbb33b241a2))

- Enhance test utilities and clean state management for improved reliability
  ([`637081a`](https://github.com/thelightfeaver/kesher/commit/637081afc0acd29d1b179429909cd26b4ca5b6e0))

- Ensure clean state function handles missing process gracefully
  ([`c16294e`](https://github.com/thelightfeaver/kesher/commit/c16294e57a9c251463a6d6c0f1e7adc1a3c453ac))

- Ensure process IDs are correctly handled as strings in termination logic
  ([`35cfa44`](https://github.com/thelightfeaver/kesher/commit/35cfa44ca4997d9f606a97efc9c4220153417883))

- Ensure process status is updated correctly upon termination and during initialization
  ([`803e1b5`](https://github.com/thelightfeaver/kesher/commit/803e1b5c120331ba3cde01448ac03d07c9d2a013))

- Handle unknown API type in start function to ensure proper execution
  ([`e9866ea`](https://github.com/thelightfeaver/kesher/commit/e9866ea6cc5114a9ac80a53c4ce36a2dd2eb5fce))

- Initialize processes dictionary in State class and update method to handle field updates
  ([`c875ac5`](https://github.com/thelightfeaver/kesher/commit/c875ac5af1673e69e03cf239ee31d979e65b5b22))

- Refactor start function to improve environment validation and clarify error messages
  ([`1556b86`](https://github.com/thelightfeaver/kesher/commit/1556b86aa46fb1a3a21c907623ba406efbbc568a))

- Remove process from info_process if not running
  ([`55f58fd`](https://github.com/thelightfeaver/kesher/commit/55f58fde695f6e0bfb1fd8affb551beed3c3fe2b))

- Remove unnecessary blank lines in the Environment class
  ([`fc468ef`](https://github.com/thelightfeaver/kesher/commit/fc468efb189b3da29432694645b18b62f7494cba))

- Remove unnecessary newline at end of file in engine.py and process.py
  ([`72c9dcb`](https://github.com/thelightfeaver/kesher/commit/72c9dcb12207678fe9ac3e60b7a4ee25f2521702))

- Rename parameter in search method for clarity and consistency
  ([`2d9eed6`](https://github.com/thelightfeaver/kesher/commit/2d9eed623e74101095bb3d87f2cf50db6d0a15a3))

- Rename terminate methods to stop for consistency in process management
  ([`dfec0a7`](https://github.com/thelightfeaver/kesher/commit/dfec0a722b8fd6303b4928cdcc5cfc5882957e5f))

- Reorder pre-commit hooks for improved configuration clarity
  ([`4dc4f91`](https://github.com/thelightfeaver/kesher/commit/4dc4f91b7a11a989eab10b744f7db746a093e850))

- Retrieve all process information when 'all' PID is specified
  ([`266a964`](https://github.com/thelightfeaver/kesher/commit/266a964b6a83c928df4a2520974a66a3b3af8842))

- Simplify condition check for process data existence in status method
  ([`0c77820`](https://github.com/thelightfeaver/kesher/commit/0c7782042b68ce5da80ef42fce707eae709c6c12))

- Simplify process not found messages for clarity
  ([`28ae861`](https://github.com/thelightfeaver/kesher/commit/28ae8615b941bb57c82b81db0e960ed32dbae431))

- Standardize parameter naming from pid to id in process management methods
  ([`6e6aa81`](https://github.com/thelightfeaver/kesher/commit/6e6aa81a60a8d043832c4bc77179e775c67e82e5))

- Streamline process stopping logic and improve status update handling
  ([`076f3a8`](https://github.com/thelightfeaver/kesher/commit/076f3a8ecfadb4f6a917cc5ac3c1b4ae0401497d))

- Update .gitignore to exclude all log and JSON files
  ([`16a78a8`](https://github.com/thelightfeaver/kesher/commit/16a78a8d3c59e3e5a067c5b646b40000b05ba5f1))

- Update Environment class to correctly handle virtual environment paths
  ([`e11f9b2`](https://github.com/thelightfeaver/kesher/commit/e11f9b240c7840a8c4a324bee414078f0e051d92))

- Update log action binding and improve log display functionality
  ([`e3f9671`](https://github.com/thelightfeaver/kesher/commit/e3f967196c2781f819eab5105a5150dfb418308d))

- Update process state checks for clarity and consistency in stop, status, and delete methods
  ([`b699882`](https://github.com/thelightfeaver/kesher/commit/b6998827fc948f62e7a713ce846e27c08e962483))

- Update process status retrieval method and correct parameter type in stop method
  ([`91d6cf8`](https://github.com/thelightfeaver/kesher/commit/91d6cf8e2ea5786ab339709535089e46f2e8aada))

- Update process termination status messages and improve memory size formatting
  ([`5ef8b35`](https://github.com/thelightfeaver/kesher/commit/5ef8b3503c704efcf09a8d356b7ce10715d6cfc1))

- Update search method to correctly handle key comparisons and improve update method logic
  ([`17578e1`](https://github.com/thelightfeaver/kesher/commit/17578e1630840bee89e2e5dca5a6add3a89a583d))

### Chores

- Add file config text editor and secret file
  ([`e306b9f`](https://github.com/thelightfeaver/kesher/commit/e306b9fb9f0f425a32e5bc413051c8f496375b92))

- Add TODO comment for error handling in process info display
  ([`b0b6ccc`](https://github.com/thelightfeaver/kesher/commit/b0b6ccc34e9a960de13f75e482d44d225949c78f))

### Code Style

- Add process.log to .gitignore to exclude log files from version control
  ([`38436e6`](https://github.com/thelightfeaver/kesher/commit/38436e637883b52dc68c693d8f1b3cecfdb02536))

- Adjust formatting and import order in engine and process modules
  ([`be6a130`](https://github.com/thelightfeaver/kesher/commit/be6a130d9d78a2309e2be9b7910e4c5d3411a203))

- Format imports consistently across multiple files
  ([`b576694`](https://github.com/thelightfeaver/kesher/commit/b57669449b195e6c45bf23233ca2d02370b72a3f))

- Format parameters in execute method for improved readability
  ([`acbf241`](https://github.com/thelightfeaver/kesher/commit/acbf24117f6c43184840f8607c9df118b9af4c9e))

- Update Environment class to use relative paths for virtual environments
  ([`2cfae34`](https://github.com/thelightfeaver/kesher/commit/2cfae34d56a7f0b5e472f8bb40cfa24071be5337))

### Documentation

- Add docstring to entry point for clarity
  ([`ee9ea0e`](https://github.com/thelightfeaver/kesher/commit/ee9ea0e81c0ec892dfe25efa3380de2fb51ca685))

- Add module docstrings for core components to enhance clarity
  ([`bddda39`](https://github.com/thelightfeaver/kesher/commit/bddda396bf865f081f92cbbd6c26cd86d716a078))

- Add WIP note for interactive monitor in README
  ([`9c1c469`](https://github.com/thelightfeaver/kesher/commit/9c1c469288971eb839c734747e04b34f8df6ec17))

- Remove unnecessary blank lines in README
  ([`ad865af`](https://github.com/thelightfeaver/kesher/commit/ad865af1332ec28f8c628250d061cb4554ba6a84))

- Update README to clarify process management features and scripts
  ([`cba4486`](https://github.com/thelightfeaver/kesher/commit/cba4486f4fb8a97e79966f3316ce4c36f946f53f))

- Update README to improve clarity on installation and command usage
  ([`ec81ab0`](https://github.com/thelightfeaver/kesher/commit/ec81ab018fd59593105c7ef8e7d12fdff9304097))

- Update README to include 'all' option for stop and status commands
  ([`6eeb9c4`](https://github.com/thelightfeaver/kesher/commit/6eeb9c43dcf9effb8361e56cc5800438da857a2a))

### Features

- Add app directory to .gitignore
  ([`cc40f48`](https://github.com/thelightfeaver/kesher/commit/cc40f48b5ebf46b8a913b04327dd0519ac9b4d13))

- Add delete command for process management and enhance docstrings
  ([`610dca0`](https://github.com/thelightfeaver/kesher/commit/610dca0c9344a4756dcc760bec7a7d3719a4d2d9))

- Add docker-compose configuration for Redis service
  ([`c36a951`](https://github.com/thelightfeaver/kesher/commit/c36a951c7bf28866940479f7eef3e5e44747033d))

- Add faker packages to dependencies in pyproject.toml and uv.lock
  ([`985aef9`](https://github.com/thelightfeaver/kesher/commit/985aef9854fbc3fcad8420132ca9dab4a705365f))

- Add get_resources method to retrieve current system resource usage
  ([`8877b34`](https://github.com/thelightfeaver/kesher/commit/8877b34e558b852d02c8f61b8d93c136bb205f11))

- Add host information to process data during execution
  ([`2a33759`](https://github.com/thelightfeaver/kesher/commit/2a337598f3cf65c391155d5069b5c5c141bc03f9))

- Add pytest and iniconfig dependencies for testing support
  ([`388ff4b`](https://github.com/thelightfeaver/kesher/commit/388ff4b25bae96a412637e651dd73a609fab2521))

- Add restart command to CLI
  ([`eaab03b`](https://github.com/thelightfeaver/kesher/commit/eaab03b8c556b959a86ffe90fe4c75466d5326ac))

- Add restart command to README and implement ProcessBase class
  ([`bc655cc`](https://github.com/thelightfeaver/kesher/commit/bc655cc8c985ec8ae1f17012f5f50633568c0419))

- Add rich library for enhanced console output and improve process info display
  ([`6993744`](https://github.com/thelightfeaver/kesher/commit/6993744b5e69c37168118f8ec401b43744a1cb5a))

- Add status command to manage process status and update Process class for tracking process states
  ([`4e6b163`](https://github.com/thelightfeaver/kesher/commit/4e6b163f5158f90ba2e57d5e6fc63fa1f3d0af17))

- Add title and subtitle to KesherMenu on mount
  ([`40632ba`](https://github.com/thelightfeaver/kesher/commit/40632ba9bf7ec3b4ea9c65f805adb76af29a6eaf))

- Add uvloop dependency for improved asynchronous performance
  ([`2848b07`](https://github.com/thelightfeaver/kesher/commit/2848b07ce878d2c6d83b959703ed109a63c6b83d))

- Create structure and create env
  ([`6356526`](https://github.com/thelightfeaver/kesher/commit/6356526f300e9ae9825db3352596373eccbca91f))

- Enhance delete command to support deleting all processes
  ([`5641551`](https://github.com/thelightfeaver/kesher/commit/56415514b4857eee1ae0dc6c382094de0d9e8d30))

- Enhance Process class to manage process data and implement termination functionality
  ([`5b2fec4`](https://github.com/thelightfeaver/kesher/commit/5b2fec489049a7c504d67ee446705544050804d7))

- Enhance process management with log folder creation and auto-start option
  ([`3585b98`](https://github.com/thelightfeaver/kesher/commit/3585b9841035f905f648637a022bcade77140107))

- Enhance process management with name and auto-start options in start command
  ([`2ecba5c`](https://github.com/thelightfeaver/kesher/commit/2ecba5c1de1ccebb208adc1dcf4ab523a870adfa))

- Implement Command class with start, stop, status, log, and delete methods; add tests for process
  management
  ([`55ff2a9`](https://github.com/thelightfeaver/kesher/commit/55ff2a9b17ebb7ffda10d43faa260b9fc8a50a83))

- Implement Daemon class for process monitoring and management
  ([`61a08ef`](https://github.com/thelightfeaver/kesher/commit/61a08ef5340e2846c0558153a81d3e188f36f30a))

- Implement Daemon class to monitor and restart processes
  ([`365494d`](https://github.com/thelightfeaver/kesher/commit/365494d0aa76720161d0a56fa14d47d943a29ab5))

- Implement Environment class and start function for application initialization
  ([`96a902d`](https://github.com/thelightfeaver/kesher/commit/96a902d970209e0e93e7b426d4568becf52e6545))

- Implement FooterWidget and HeaderWidget classes; restructure KesherMenu
  ([`4181744`](https://github.com/thelightfeaver/kesher/commit/41817447a983aafac68d653f7a0f089bc63951ec))

- Implement KesherMenu class and update main application entry point
  ([`95524a3`](https://github.com/thelightfeaver/kesher/commit/95524a3d5cbdaa372e7f8f58bd527d9a37ba9392))

- Implement Process class for managing system processes
  ([`9b53793`](https://github.com/thelightfeaver/kesher/commit/9b5379372cab26c727151c90d9e18fc067c8b7f1))

- Implement process restart functionality and improve process management
  ([`a731e72`](https://github.com/thelightfeaver/kesher/commit/a731e723213e18ad45a6e30d7eec825e939a1edd))

- Implement State class for process state management and refactor Process class to utilize it
  ([`f5e78af`](https://github.com/thelightfeaver/kesher/commit/f5e78af3cc6a49e1473ff99f379b9908da861193))

- Initialize core, models, and util modules with necessary imports and exports
  ([`d0eae67`](https://github.com/thelightfeaver/kesher/commit/d0eae6762dd4f418772319c6329757fbee5d13d2))

- Initialize versioning in __init__.py
  ([`b3e3087`](https://github.com/thelightfeaver/kesher/commit/b3e3087036121a01f99b76119a00d70b2550537f))

- Main.py to set executable permissions
  ([`01f4d56`](https://github.com/thelightfeaver/kesher/commit/01f4d560541af84c943af0e0d214e1d3759613ad))

- Restructure entry point and implement CLI commands for Kesher
  ([`d6fd9ad`](https://github.com/thelightfeaver/kesher/commit/d6fd9ad3e088c4cb75d4c3e7dafae4a7d320e26d))

- Round memory size to MB and add to process info table
  ([`5177f63`](https://github.com/thelightfeaver/kesher/commit/5177f63fb2a20b92021ed6299ec272f25bbb78b2))

- Update .gitignore to include .ruff_cache and ensure data.json is correctly listed
  ([`c859a85`](https://github.com/thelightfeaver/kesher/commit/c859a859750f8d6ce82ed793c449f9cb1c6c3df4))

- Update .gitignore to include data.json and ensure issue.md is listed correctly
  ([`b17c4db`](https://github.com/thelightfeaver/kesher/commit/b17c4db1f2d440b7ab21dfc81b3c6975f71c52dc))

- Update click dependency in pyproject.toml and uv.lock
  ([`3f92a96`](https://github.com/thelightfeaver/kesher/commit/3f92a96eb26fed863ae6c30970c3083f2755d01c))

- Update execute method to accept a custom name for the process
  ([`0c4a073`](https://github.com/thelightfeaver/kesher/commit/0c4a0738ab1f209c77424b3382352f61cc8d9746))

### Refactoring

- Add additional pre-commit hooks for enhanced code quality checks
  ([`bb1338f`](https://github.com/thelightfeaver/kesher/commit/bb1338f2a397066f61e8dae396e4fa003c83a6cf))

- Add additional pre-commit hooks for improved code quality checks
  ([`2a931a3`](https://github.com/thelightfeaver/kesher/commit/2a931a32b1da8200991016ca1bb037eb549d856e))

- Add class docstring for Process to improve code documentation
  ([`c91a995`](https://github.com/thelightfeaver/kesher/commit/c91a99555adadc29f6e7501bc651cab26f411b93))

- Add conventional pre-commit hook for improved commit message standards
  ([`b2129e3`](https://github.com/thelightfeaver/kesher/commit/b2129e38d2728a205e06ba29ef1e4436f4dcc094))

- Add help descriptions to CLI commands in entry point
  ([`44084ee`](https://github.com/thelightfeaver/kesher/commit/44084eefc8062e480bbdc5a5f39b0863e5a01f26))

- Add resource table container and implement process deletion functionality
  ([`808d2af`](https://github.com/thelightfeaver/kesher/commit/808d2af7763adf2f082e3af5f72ec9ecba1f01f3))

- Add resource table container and update log display functionality
  ([`e95f88a`](https://github.com/thelightfeaver/kesher/commit/e95f88ad9e0936a62cc2c7b86c502ea55be0a281))

- Clean up command list formatting and streamline stop and log functions
  ([`5fb51c6`](https://github.com/thelightfeaver/kesher/commit/5fb51c66712aa287f1e986a849a4542f552e2cdf))

- Clean up engine and entry point code structure
  ([`0a36095`](https://github.com/thelightfeaver/kesher/commit/0a360952c06867fa823ef178e908de34af087d12))

- Clean up imports and improve code formatting in core modules
  ([`a583197`](https://github.com/thelightfeaver/kesher/commit/a583197bfadcd537ed781c47daa5bd694e5f5451))

- Clean up monitor.py by removing unnecessary blank lines and unused code
  ([`e386962`](https://github.com/thelightfeaver/kesher/commit/e3869622cb9fff9a3e49a2669c4d97d2d3c6ee8b))

- Clean up whitespace in load_resource method
  ([`7f698f9`](https://github.com/thelightfeaver/kesher/commit/7f698f90bff8083d93c019c6b63b7e96ec3bbe45))

- Enhance feature list formatting in README.md with emojis
  ([`73e38b7`](https://github.com/thelightfeaver/kesher/commit/73e38b76869f50f90fee3b9a563ee2d6a4ef9674))

- Enhance log display functionality and update log refresh interval
  ([`b7c404c`](https://github.com/thelightfeaver/kesher/commit/b7c404cd46ac76800d12b0e54444f0b8bc19c43f))

- Enhance process management by adding start_time and version_interpreter attributes to ProcessBase
  ([`884dcce`](https://github.com/thelightfeaver/kesher/commit/884dccef869cca668812f640a1b023872e37e7cd))

- Enhance process monitoring logic to handle stopped processes with disabled auto-start
  ([`286f48d`](https://github.com/thelightfeaver/kesher/commit/286f48d824cb4d7ab04b38bbd5fc57d1f949ebe2))

- Enhance resource monitoring and display functionality in the UI
  ([`90b01da`](https://github.com/thelightfeaver/kesher/commit/90b01da97fad62b1fc611fddf31a2a1b95fb5fc0))

- Improve log method formatting and enhance log display functionality
  ([`4c14e51`](https://github.com/thelightfeaver/kesher/commit/4c14e51cb8d60f83fc11d4bc783253d56d350bfb))

- Improve readability by reorganizing comments in status process test
  ([`874557b`](https://github.com/thelightfeaver/kesher/commit/874557b8f58b74c22623b8f796ed50cdeda99fa3))

- Rearrange state file initialization and enhance load method error handling
  ([`bb89e70`](https://github.com/thelightfeaver/kesher/commit/bb89e70898744139b94e5894e68cc85ff21f1b79))

- Remove log binding and update log display functionality to show logs for selected process
  ([`f51e758`](https://github.com/thelightfeaver/kesher/commit/f51e758ff867083fcbbbd8e2eeb1d440ab12f308))

- Remove main execution block from State class
  ([`6a52321`](https://github.com/thelightfeaver/kesher/commit/6a52321abca037b53fe1cada1ea41c8326e86d8a))

- Remove unnecessary blank lines in pre-commit configuration
  ([`092112d`](https://github.com/thelightfeaver/kesher/commit/092112d6d0589a961c9566eddd6461bfb53df5fe))

- Remove unused FooterWidget and HeaderWidget, integrate directly into KesherMenu
  ([`ddefe62`](https://github.com/thelightfeaver/kesher/commit/ddefe624706b20c5149c8c09405588c17142e73e))

- Remove unused json import and _save_data method from Environment class
  ([`6cbb8ae`](https://github.com/thelightfeaver/kesher/commit/6cbb8aecf7ea8654f1fd0a6bb99cd262e5560ee4))

- Rename execute method to start in Process class
  ([`193aace`](https://github.com/thelightfeaver/kesher/commit/193aace64aceb7c00446a33ac53a61e302067520))

- Rename execute method to start in Process class and update usage in engine
  ([`d6ce681`](https://github.com/thelightfeaver/kesher/commit/d6ce6814953971ed4b07d0a996d32c3064af6e07))

- Rename KesherMenu to KesherTUI for consistency in UI components
  ([`c958775`](https://github.com/thelightfeaver/kesher/commit/c9587754c13c598fbc8781d83fe0d944f5d64b9d))

- Reorganize imports and streamline process stopping logic
  ([`9fee3d3`](https://github.com/thelightfeaver/kesher/commit/9fee3d3bdb39182c4f222a8523edd07943fcd36e))

- Replace log action with load_log method and update log refresh callback
  ([`dd3c73c`](https://github.com/thelightfeaver/kesher/commit/dd3c73c76e7e413b9f63971376589eb12ec06ce8))

- Replace os.system calls with Process execution for better control
  ([`95c8885`](https://github.com/thelightfeaver/kesher/commit/95c88856371f181389188fe0ddf8ffd3d297f714))

- Restructure layout by replacing Container with Horizontal and Vertical for improved UI
  organization
  ([`2f5b0d9`](https://github.com/thelightfeaver/kesher/commit/2f5b0d9e7ed83d9909e0c16ae98952c330e19c03))

- Restructure process monitoring logic and improve status checks
  ([`131899a`](https://github.com/thelightfeaver/kesher/commit/131899ae68fb51041dce8dd157014e563f574113))

- Simplify process data handling by using underscore for unused variables
  ([`ed0635e`](https://github.com/thelightfeaver/kesher/commit/ed0635e07857ca72f57898d9d270453da1174892))

- Streamline command execution in start function and improve readability
  ([`a1dcbaf`](https://github.com/thelightfeaver/kesher/commit/a1dcbaf2c31eb55b234258d5daea2a507468a152))

- Update .gitignore to include additional distribution files
  ([`02a7041`](https://github.com/thelightfeaver/kesher/commit/02a7041ddf6f8af82b13c226af01c1e872d1e073))

- Update Daemon class to improve process monitoring and adjust sleep duration
  ([`e0870aa`](https://github.com/thelightfeaver/kesher/commit/e0870aab5bd01b2c349da513c75e852117277cf8))

- Update FooterWidget to inherit from Widget and customize Footer display
  ([`8b040b6`](https://github.com/thelightfeaver/kesher/commit/8b040b6183c2cc7990a4aadf3ec52b4e3ffbe1cf))

- Update log method to return log content and remove unnecessary comment
  ([`9142c89`](https://github.com/thelightfeaver/kesher/commit/9142c895b397ec30da93ef877f126c104233727d))

- Update log method to return None instead of log content
  ([`a9b2a4a`](https://github.com/thelightfeaver/kesher/commit/a9b2a4af99e930c7e3a40d197cce92db501b7c6f))

- Update pre-commit configuration and improve condition check in process deletion
  ([`708ed0d`](https://github.com/thelightfeaver/kesher/commit/708ed0d8e89d7a3e244d691e1b11212bc6e93dc1))

- Update process management logic in Daemon and improve file path assignment in Environment
  ([`38fdffd`](https://github.com/thelightfeaver/kesher/commit/38fdffd2517bb06994f65e08f596d4fa6ecaacaa))

- Update process management logic to use state and improve cleanup
  ([`7e63f96`](https://github.com/thelightfeaver/kesher/commit/7e63f96affad11c0eb13d6eac1c7a11ab745cccf))

- Update process status check to handle empty dictionary case
  ([`1cd9c70`](https://github.com/thelightfeaver/kesher/commit/1cd9c7087942b83714cc8ad39b3d4660a67ff25b))

- Update start method to remove return value and improve clarity
  ([`b5d41b4`](https://github.com/thelightfeaver/kesher/commit/b5d41b44cf41c6bf532b2c2de95fde1cc15283b7))

### Testing

- Add process deletion test and ensure process state is updated
  ([`72de8ba`](https://github.com/thelightfeaver/kesher/commit/72de8bacc47fcd0380fe04712a4171db1c8394bb))

- Add status process test to verify process start and status
  ([`ac66262`](https://github.com/thelightfeaver/kesher/commit/ac66262ca1fcac475f6186df9ef617345bc67db3))
