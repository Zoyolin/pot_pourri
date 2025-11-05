/*Area51
g++ -std=c++17 $(realpath $0) -o $(basename $0).run \
&& $(dirname $(realpath $0))/$(basename $0).run

exit
*/

#include <iostream>
#include <string>
#include <sysexits.h>
#include <errno.h>
#include <iterator>
#include <filesystem>
#include <locale>

void debug_print(auto it, auto last, auto path_out)
{
    static int step=0;
    std::cout << "step " << step << std::endl;
    std::cout << "it " << (*it).string() << std::endl;
    if (last != nullptr)
        std::cout << "last " << (*last).string() << std::endl;
    std::cout << "path_out " << path_out.string() << std::endl << std::endl;
}

error_t main(int argc, char *argv[])
{
    if (argc == 1)
    {
        std::filesystem::path thisfile(argv[0]);
        std::cout << "Usage:  " << thisfile.filename().string() << " <path> " << std::endl;
        return EX_USAGE;
    }
    if (argc != 2)
    {
        return EX_USAGE;
    }

    std::string str_input(argv[1]);
    std::filesystem::path path_out;

    // trim whitespaces
    std::string whitespaces = " \t\n\v\f\r";
    str_input.erase(0, str_input.find_first_not_of(whitespaces));
    str_input.erase(str_input.find_last_not_of(whitespaces) + 1);

    std::filesystem::path path_in(str_input);

    // path_in = path_in.remove_filename();

    auto last = path_in.end();
    auto it = path_in.begin();

    debug_print(it, nullptr, path_out);
    
    if (it == path_in.end())
    { // case of relative filename 'cool_file' or empty string '""'
        std::cout << path_in.string();
        return 0;
    }
    std::advance(last, -1);
    
    debug_print(it, last, path_out);
    
    // std::cout << "last  " <<(*last).string() << std::endl;
    if (it == last)
    { // case of root folder '/cool_file'
        std::cout << path_in.string();
        return 0;
    }
    
    debug_print(it, last, path_out);
    
    // std::advance(last, -1);
    // std::cout << "last  " <<(*last).string() << std::endl;
    // if (it == last)
    // { // case of a single relative folder 'dir1/cool_file'
    //     std::cout << path_in.string();
    //     return 0;
    // }
    
    if (path_in.is_relative())
        path_out.append((*it).string());
    else
        path_out /= (*it).string().substr(0, 3);
    
    // std::cout << path_out.string() << std::endl;
    std::advance(it, 1);
    
    debug_print(it, last, path_out);
    
    while (it != last){
        // std::cout << "loop  0 " <<(*it).string() << std::endl;
        path_out /= (*it).string().substr(0, 3);
        std::advance(it, 1);
        
        debug_print(it, last, path_out);
    }

    // std::cout << (*path_in.begin()).string() << std::endl;
    // std::cout << (*last).string() << std::endl;
    if (path_in.begin() != last)
        path_out.append((*last).string());

    std::cout << path_out.string();
    return 0;
}