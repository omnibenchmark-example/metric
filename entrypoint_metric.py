import argparse
import os


def concatenate_input_content(input_files):
    content = ""
    for input_file in input_files:
        with open(input_file, 'r') as file:
            content += file.read() + '\n'
    return content


def main():
    parser = argparse.ArgumentParser(description='Run metric on files.')
    parser.add_argument('--output_dir', type=str, help='output directory where metric will store results.')
    parser.add_argument('--name', type=str, help='name of the module')
    # api >= 0.8.0: the exact path to write, as `--output <id>=PATH`. The stage
    # declares one output, whatever the benchmark calls it.
    parser.add_argument('--output', action='append', default=[], help='id=PATH of the output to write')
    parser.add_argument('--methods.mapping', type=str, help='input file #1.')
    parser.add_argument('--data.meta', type=str, help='input file #2.')
    parser.add_argument('--data.data_specific_params', type=str, help='input file #3.', required=False)
    args, _ = parser.parse_known_args()

    inputs = [getattr(args, 'methods.mapping'), getattr(args, 'data.meta'), getattr(args, 'data.data_specific_params')]
    input_files = [f for f in inputs if f]

    if args.output:
        results_file = args.output[0].split("=", 1)[1]
    else:
        results_file = os.path.join(args.output_dir, f'{args.name}.results.txt')

    content = concatenate_input_content(input_files)
    content += f"4. Running metric using parameters into {results_file}"

    os.makedirs(os.path.dirname(results_file) or ".", exist_ok=True)
    with open(results_file, 'w') as file:
        file.write(content)


if __name__ == "__main__":
    main()
