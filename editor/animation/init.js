//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        function sevenSegmentCanvas(dom, input) {
            const segs = 'ABCDEFGabcdefg'.split('');
            const paper = Raphael(dom, 220, 180, 0, 0); 
            const draw_segment = (sx, sy, z, f)=>{
                const attr = {
                    seg: {
                        fill: '#dfe8f7',
                        'stroke-width': 0.2,

                    },
                    font: {
                        'font-size': 15*z
                    },
                };
                const s_set = paper.set();

                for (let i=0; i < 2; i += 1) {
                    const s_a = paper.path(
                            'M' + (sx+i * (110*z)) + ',' + sy +
                            "l" + (10*z) + ',' + (-10*z) +
                            "l" + (50*z) + ',' + (0*z) + 
                            'l' + (10*z) + ',' + (10*z) +
                            'l' + (-10*z) + ',' + (10*z) +
                            'l' + (-50*z) + ',0Z').attr(attr.seg);
                    s_set.push(s_a);
                    const seg_params = [
                        [35, 35, 90],
                        [35, 105, 90],
                        [0, 140, 0],
                        [-35, 105, 90],
                        [-35, 35, 90],
                        [0, 70, 0]
                    ];
                    for (let k=0; k < 6; k+= 1){
                        const [dx, dy, rt] = seg_params[k];
                        s_set.push(s_a.clone().transform(
                            't'+(dx*z)+','+(dy*z)+'r'+rt));
                    }
                }

                if (! f)
                    return s_set;

                for (let i=0; i < 2; i += 1) {
                    const os = i * (110*z);
                    const [a, b, c, d, e, f, g] = segs.slice(0+i*7, 7+i*7);
                    const fig_params = [
                        [35, 0, a],
                        [70, 35, b], 
                        [70, 105, c], 
                        [35, 140, d], 
                        [0, 105, e], 
                        [0, 35, f],
                        [35, 70, g]
                    ];
                    for (let j=0; j < 7; j+=1){
                        const [dx, dy, sg] = fig_params[j];
                        s_set.push(
                                paper.text(sx+os+dx*z, sy+dy*z, sg)).attr(
                                    attr.font);
                    }
                }
                return s_set;
            };

            const display_segments = (ss, lits, broken)=>{
                lits.split('').forEach(s=>{
                    ss[segs.indexOf(s)].attr("fill", "#FAA200");
                });

                broken.split('').forEach(s=>{
                    ss[segs.indexOf(s)].animate({"fill": "#8FC7ED"}, 1000);
                });
            };

            display_segments(
                draw_segment(20, 20, 1, 1),
                input[0].join(''),
                input[1].join('')
            );
        }

        let $tryit;
        let io = new extIO({
            multipleArguments: true,
            functions: {
                js: 'sevenSegment',
                python: 'seven_segment'
            },
            animation: function($expl, data){
                sevenSegmentCanvas(
                    $expl[0],
                    data.in
                );
            }
        });
        io.start();
    }
);
